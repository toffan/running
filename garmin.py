import enum
import functools
import itertools
import json
import logging
import os
import typing as t
from collections import defaultdict
from datetime import date
from datetime import timedelta

import requests

from plans import marathon
from workouts import Cooldown
from workouts import Recovery
from workouts import Repeat
from workouts import Segment
from workouts import Step
from workouts import Warmup
from workouts import Workout


class SportType(enum.Enum):
    RUNNING = 1
    CYCLING = 2
    OTHER = 3
    SWIMMING = 4
    STRENGTH_TRAINING = 5
    CARDIO_TRAINING = 6
    YOGA = 7
    PILATES = 8
    HIIT = 9


class StepType(enum.Enum):
    WARMUP = 1
    COOLDOWN = 2
    INTERVAL = 3
    RECOVERY = 4
    REST = 5
    REPEAT = 6
    OTHER = 7
    MAIN = 8


def getType(seg: Step) -> StepType:
    if isinstance(seg, Warmup):
        return StepType.WARMUP
    elif isinstance(seg, Cooldown):
        return StepType.COOLDOWN
    elif isinstance(seg, Recovery):
        return StepType.RECOVERY
    elif isinstance(seg, Repeat):
        return StepType.REPEAT
    else:
        return StepType.INTERVAL


class EndCondition(enum.Enum):
    LAP_BUTTON = 1  # no value
    TIME = 2  # in seconds
    DISTANCE = 3  # in meters
    CALORIES = 4
    POWER = 5
    HEART_RATE = 6
    ITERATIONS = 7
    FIXED_REST = 8
    FIXED_REPETITIONS = 9
    REPS = 10
    TRAINING_PEAKS_TSS = 11
    REPETITION_TIME = 12
    TIME_AT_VALID_CDA = 13
    POWER_LAST_LAP = 14
    MAX_POWER_LAST_LAP = 15
    REPETITION_SWIM_CSS_OFFSET = 16


class Intensity(enum.Enum):
    ACTIVE = 1
    REST = 2
    WARMUP = 3
    COOLDOWN = 4


def make_endCondition(seg: Step) -> dict[str, t.Any]:
    if isinstance(seg, Repeat):
        return {
            "endCondition": {
                "conditionTypeId": EndCondition.ITERATIONS.value,
            },
            "numberOfIterations": seg.count,
        }

    elif isinstance(seg.duration, timedelta):
        return {
            "endCondition": {
                "conditionTypeId": EndCondition.TIME.value,
            },
            "endConditionValue": int(seg.duration.total_seconds()),
        }

    else:
        return {
            "endCondition": {
                "conditionTypeId": EndCondition.DISTANCE.value,
            },
            "endConditionValue": int(seg.duration * 1000),
        }


class TargetType(enum.Enum):
    NO_TARGET = 1
    POWER_ZONE = 2
    CADENCE = 3
    SPEED_ZONE = 5
    HEART_RATE = 4  # in beat per minute
    PACE = 6  # in meters per seconds
    GRADE = 7
    HEART_RATE_LAP = 8
    POWER_LAP = 9
    POWER_3S = 10
    POWER_10S = 11
    POWER_30S = 12
    SPEED_LAP = 13
    SWIM_STROKE = 14
    RESISTANCE = 15
    POWER_CURVE = 16
    SWIM_CSS_OFFSET = 17
    SWIM_INSTRUCTION = 18


def make_targetType(seg: Segment) -> dict[str, t.Any]:
    if isinstance(seg, (Warmup, Cooldown, Recovery)):
        # Do not enforce HR target for warmup, cooldown and recovery.
        return {}

    dct: dict[str, t.Any] = {
        "targetType": {
            "workoutTargetTypeId": TargetType.HEART_RATE.value,
        }
    }
    if seg.hr.number is not None:
        dct.update({"zoneNumber": str(seg.hr.number)})
    else:
        dct.update(
            {
                "targetValueOne": seg.hr.low,
                "targetValueTwo": seg.hr.high,
            }
        )
    return dct


class GarminSerializer:
    def __init__(self) -> None:
        self.stepId = itertools.count(1)

    def serialize(self, workout: Workout) -> str:
        # stepId count is local to the current Workout
        self.stepId = itertools.count(1)
        dct = {
            "sportType": {
                "sportTypeId": SportType.RUNNING.value,
            },
            "workoutName": workout.name,
            "workoutSegments": [
                {
                    "sportType": {
                        "sportTypeId": SportType.RUNNING.value,
                    },
                    "workoutSteps": [self._serialize(seg) for seg in workout.steps],
                },
            ],
        }

        return json.dumps(dct)

    @functools.singledispatchmethod
    def _serialize(self, arg) -> dict:
        raise NotImplementedError(f"Cannot serialize a {arg.__class__.__name__}")

    @_serialize.register
    def _(self, step: Segment) -> dict:
        dct = {
            "type": "ExecutableStepDTO",
            "stepOrder": next(self.stepId),
            "stepType": {
                "stepTypeId": getType(step).value,
            },
        }
        if step.notes is not None:
            dct["description"] = step.notes
        dct.update(make_targetType(step))
        dct.update(make_endCondition(step))

        return dct

    @_serialize.register
    def _(self, repeat: Repeat) -> dict:
        dct = {
            "type": "RepeatGroupDTO",
            "stepOrder": next(self.stepId),
            "stepType": {
                "stepTypeId": getType(repeat).value,
            },
            "workoutSteps": [],
        }
        dct.update(make_endCondition(repeat))
        for step in repeat.steps:
            dct["workoutSteps"].append(self._serialize(step))

        return dct


class GarminConnect:

    BASE_URL = "https://connect.garmin.com"

    def __init__(
        self,
        token: str,
        cookies: dict[str, str] | str,
        logger: logging.Logger = logging.getLogger(__name__),
    ) -> None:
        self.log = logger

        self.workouts: dict[str, list[int]] = defaultdict(list)
        self.serializer = GarminSerializer()

        self.session = requests.Session()
        self.session.headers["Authorization"] = token.strip()
        self.session.headers["Content-Type"] = "application/json;charset=utf-8"
        self.session.headers["DI-Backend"] = "connectapi.garmin.com"

        if isinstance(cookies, str):
            cookies = dict(c.split("=") for c in cookies.strip().split("; "))
        self.session.cookies.update(cookies)

    def login(self) -> None:
        # Does not work
        # TODO: retrieve cookies automatically
        self.log.info("Logging in.")
        response = self.session.get("https://connect.garmin.com/modern/")
        self.log.debug("Response: %r", response)

    def load(self) -> None:
        self.log.info("Load all workouts.")

        url = f"{self.BASE_URL}/workout-service/workouts"
        params = {
            "start": 1,
            "limit": 999,
            "myWorkoutsOnly": True,
            "includeAtp": False,
        }
        response = self.session.get(url, params=params)
        for workout in response.json():
            self.workouts[workout["workoutName"]].append(workout["workoutId"])

    def delete(self, workout: Workout | str) -> None:
        name = workout.name if isinstance(workout, Workout) else workout

        for workoutId in self.workouts.get(name, []):
            self.log.info("Delete '%s' (id: %d)", name, workoutId)

            url = f"{self.BASE_URL}/workout-service/workout/{workoutId}"
            headers = {"X-HTTP-Method-Override": "DELETE"}
            self.session.post(url, headers=headers)

    def delete_all(self) -> None:
        self.log.info("Delete all workouts.")
        for name in self.workouts.keys():
            self.delete(name)

    def save(self, workout: Workout, force=False) -> None:
        if not force and workout.name in self.workouts:
            self.log.debug(
                "Workout %r (id: %s) already exists.",
                workout.name,
                self.workouts[workout.name],
            )
            return

        self.log.info("Save '%s'", workout.name)
        url = f"{self.BASE_URL}/workout-service/workout"
        data = self.serializer.serialize(workout)
        response = self.session.post(url, data=data)
        if response.status_code != 200:
            self.log.error(
                "Received code: %d %s", response.status_code, response.reason
            )
            return
        workoutId = response.json()["workoutId"]
        self.log.debug("Saved workout %r (id: %d)", workout.name, workoutId)
        self.workouts[workout.name].append(workoutId)

    def schedule(self, workout: Workout, d: date, save=True) -> None:
        self.log.info("Schedule '%s' on %s", workout.name, d.isoformat())
        if save:
            self.save(workout, force=False)

        assert workout.name in self.workouts
        workoutId = self.workouts[workout.name][0]

        url = f"{self.BASE_URL}/workout-service/schedule/{workoutId}"
        data = {"date": d.isoformat()}
        self.session.post(url, json=data)

    def schedule_many(
        self, workouts: t.Iterable[Workout | None], start_date: date, save=True
    ) -> None:
        for i, workout in enumerate(workouts):
            if workout is not None:
                d = start_date + timedelta(days=i)
                self.schedule(workout, d=d, save=save)


if __name__ == "__main__":
    log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
    logging.basicConfig(level=log_level)

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--token",
        required=True,
        metavar="FILE",
        type=argparse.FileType("r"),
        help="File containing a valid token.",
    )
    parser.add_argument(
        "-c",
        "--cookies",
        required=True,
        metavar="FILE",
        type=argparse.FileType("r"),
        help="File containing valid cookies.",
    )

    args = parser.parse_args()
    token = args.token.read()
    cookies = args.cookies.read()

    garmin = GarminConnect(token=token, cookies=cookies)
    # garmin.login()
    garmin.load()

    ###  EDIT HERE  ###
    workouts = itertools.chain.from_iterable(marathon[1][i] for i in range(1, 5))
    garmin.schedule_many(workouts, start_date=date(2024, 12, 9))

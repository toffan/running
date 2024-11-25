import enum
import functools
import itertools
import json
import typing as t
from datetime import timedelta

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
    REPEAT = 6


def getType(seg: Segment) -> StepType:
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
    ITERATIONS = 7


def make_endCondition(seg: Segment) -> dict[str, t.Any]:
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
    HEART_RATE = 4  # in beat per minute
    PACE = 6  # in meters per seconds


def make_targetType(step: Step) -> dict[str, t.Any]:
    return {
        "targetType": {
            "workoutTargetTypeId": TargetType.HEART_RATE.value,
        },
        "targetValueOne": step.hr.low,
        "targetValueTwo": step.hr.high,
    }


class GarminConnect:
    def __init__(self) -> None:
        self.stepId = itertools.count(1)
        self.workouts: dict[Workout, int] = {}

    def serialize(self, workout: Workout, name: str) -> str:
        # stepId count is local to the current Workout
        self.stepId = itertools.count(1)
        dct = {
            "sportType": {
                "sportTypeId": SportType.RUNNING.value,
            },
            "workoutName": name,
            "workoutSegments": [
                {
                    "sportType": {
                        "sportTypeId": SportType.RUNNING.value,
                    },
                    "workoutSteps": [self._serialize(seg) for seg in workout],
                },
            ],
        }

        return json.dumps(dct)

    @functools.singledispatchmethod
    def _serialize(self, arg) -> dict:
        raise NotImplementedError(f"Cannot serialize a {arg.__class__.__name__}")

    @_serialize.register
    def _(self, step: Step) -> dict:
        dct = {
            "type": "ExecutableStepDTO",
            "stepOrder": next(self.stepId),
            "stepType": {
                "stepTypeId": getType(step).value,
            },
        }
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

    # def schedule(self, workout:Workout, d: date) -> None:
    #     dct = {"date": d.isoformat()}


### Example request
# Both warmup and cooldown are optional
#
# {
#   "sportType": {
#     "sportTypeId": 1
#   },
#   "workoutName": "Tata",
#   "workoutSegments": [
#     {
#       "sportType": {
#         "sportTypeId": 1
#       },
#       "workoutSteps": [
#         {
#           "stepOrder": 1,
#           "stepType": {
#             "stepTypeId": 1
#           },
#           "type": "ExecutableStepDTO",
#           "endCondition": {
#             "conditionTypeId": 1
#           },
#           "targetType": {
#             "workoutTargetTypeId": 1
#           }
#         },
#         {
#           "stepOrder": 2,
#           "stepType": {
#             "stepTypeId": 3
#           },
#           "type": "ExecutableStepDTO",
#           "endCondition": {
#             "conditionTypeId": 2
#           },
#           "endConditionValue": 300,  // in seconds
#           "targetType": {
#             "workoutTargetTypeId": 6
#           },
#           "targetValueOne": 4.166666666666667,  // in meters per second
#           "targetValueTwo": 2.0
#         },
#         {
#           "stepOrder": 3,
#           "stepType": {
#             "stepTypeId": 6
#           },
#           "numberOfIterations": 3,
#           "smartRepeat": false,
#           "workoutSteps": [
#             {
#               "stepOrder": 4,
#               "stepType": {
#                 "stepTypeId": 3
#               },
#               "type": "ExecutableStepDTO",
#               "endCondition": {
#                 "conditionTypeId": 3
#               },
#               "endConditionValue": 1000,  // in meters
#               "targetType": {
#                 "workoutTargetTypeId": 4
#               },
#               "targetValueOne": 120,  // in beat per minute
#               "targetValueTwo": 130
#             },
#             {
#               "stepOrder": 5,
#               "stepType": {
#                 "stepTypeId": 4
#               },
#               "type": "ExecutableStepDTO",
#               "endCondition": {
#                 "conditionTypeId": 1
#               },
#               "targetType": {
#                 "workoutTargetTypeId": 1
#               }
#             }
#           ],
#           "endCondition": {
#             "conditionTypeId": 7
#           },
#           "type": "RepeatGroupDTO"
#         },
#         {
#           "stepOrder": 6,
#           "stepType": {
#             "stepTypeId": 2
#           },
#           "type": "ExecutableStepDTO",
#           "endCondition": {
#             "conditionTypeId": 1
#           },
#           "targetType": {
#             "workoutTargetTypeId": 1
#           }
#         }
#       ]
#     }
#   ]
# }

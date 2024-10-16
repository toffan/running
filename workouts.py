from datetime import timedelta


LTHR = 170
"Lactate Threshold Heart Rate"


class HRZone:
    def __init__(self, name: str, low: float, high: float) -> None:
        self.name = name
        self.low = low * LTHR
        self.high = high * LTHR

    def __str__(self) -> str:
        return f"{self.name} [{self.low:.0f}-{self.high:.0f}]"

    def __hash__(self) -> int:
        return hash((self.name, self.low, self.high))


HR = {
    1: HRZone("Low Aerobic", 0.75, 0.80),
    2: HRZone("Moderate Aerobic", 0.81, 0.89),
    3: HRZone("Threshold", 0.96, 1),
    4: HRZone("VO2 max", 1.02, 1.05),
    5: HRZone("Speed", 1.06, 1.1),
}
HR1 = HR[1]
HR2 = HR[2]
HR3 = HR[3]
HR4 = HR[4]
HR5 = HR[5]


def min(minutes: float) -> timedelta:
    return timedelta(minutes=minutes)


class distance(float):
    pass


def mile(miles: float) -> distance:
    return distance(miles * 1.61)


class Step:
    def __init__(
        self, duration: timedelta | distance, hr: HRZone, notes: str | None = None
    ) -> None:
        self.duration = duration
        self.hr = hr
        self.notes = notes

    def __hash__(self) -> int:
        return hash((self.duration, self.hr, self.notes))


class Repeat:
    def __init__(self, count: int, steps: list[Step]) -> None:
        self.count = count
        self.steps = steps

    def __hash__(self) -> int:
        return hash((self.count, self.steps))


type Segment = Step | Repeat
type Workout = list[Segment]

recovery_run: dict[int, Workout] = {
    1: [Step(min(20), HR1)],
    2: [Step(min(25), HR1)],
    3: [Step(min(30), HR1)],
    4: [Step(min(35), HR1)],
    5: [Step(min(40), HR1)],
    6: [Step(min(45), HR1)],
    7: [Step(min(50), HR1)],
    8: [Step(min(55), HR1)],
    9: [Step(min(60), HR1)],
}

foundation_run: dict[int, Workout] = {
    1: [Step(min(5), HR1), Step(min(10), HR2), Step(min(5), HR1)],
    2: [Step(min(5), HR1), Step(min(15), HR2), Step(min(5), HR1)],
    3: [Step(min(5), HR1), Step(min(20), HR2), Step(min(5), HR1)],
    4: [Step(min(5), HR1), Step(min(25), HR2), Step(min(5), HR1)],
    5: [Step(min(5), HR1), Step(min(30), HR2), Step(min(5), HR1)],
    6: [Step(min(5), HR1), Step(min(35), HR2), Step(min(5), HR1)],
    7: [Step(min(5), HR1), Step(min(40), HR2), Step(min(5), HR1)],
    8: [Step(min(5), HR1), Step(min(45), HR2), Step(min(5), HR1)],
    9: [Step(min(5), HR1), Step(min(50), HR2), Step(min(5), HR1)],
}

long_run: dict[int, Workout] = {
    1: [Step(mile(1), HR1), Step(mile(4.5), HR2), Step(mile(0.5), HR1)],
    2: [Step(mile(1), HR1), Step(mile(5.5), HR2), Step(mile(0.5), HR1)],
    3: [Step(mile(1), HR1), Step(mile(6.5), HR2), Step(mile(0.5), HR1)],
    4: [Step(mile(1), HR1), Step(mile(7.5), HR2), Step(mile(0.5), HR1)],
    5: [Step(mile(1), HR1), Step(mile(8.5), HR2), Step(mile(0.5), HR1)],
    6: [Step(mile(1), HR1), Step(mile(9.5), HR2), Step(mile(0.5), HR1)],
    7: [Step(mile(1), HR1), Step(mile(10.5), HR2), Step(mile(0.5), HR1)],
    8: [Step(mile(1), HR1), Step(mile(11.5), HR2), Step(mile(0.5), HR1)],
    9: [Step(mile(1), HR1), Step(mile(12.5), HR2), Step(mile(0.5), HR1)],
    10: [Step(mile(1), HR1), Step(mile(13.5), HR2), Step(mile(0.5), HR1)],
    11: [Step(mile(1), HR1), Step(mile(14.5), HR2), Step(mile(0.5), HR1)],
    12: [Step(mile(1), HR1), Step(mile(15.5), HR2), Step(mile(0.5), HR1)],
    13: [Step(mile(1), HR1), Step(mile(16.5), HR2), Step(mile(0.5), HR1)],
    14: [Step(mile(1), HR1), Step(mile(17.5), HR2), Step(mile(0.5), HR1)],
    15: [Step(mile(1), HR1), Step(mile(18.5), HR2), Step(mile(0.5), HR1)],
}

fast_finish_run: dict[int, Workout] = {
    1: [Step(min(5), HR1), Step(min(15), HR2), Step(min(5), HR3)],
    2: [Step(min(5), HR1), Step(min(20), HR2), Step(min(5), HR3)],
    3: [Step(min(5), HR1), Step(min(20), HR2), Step(min(10), HR3)],
    4: [Step(min(5), HR1), Step(min(25), HR2), Step(min(10), HR3)],
    5: [Step(min(5), HR1), Step(min(25), HR2), Step(min(12), HR3)],
    6: [Step(min(5), HR1), Step(min(30), HR2), Step(min(12), HR3)],
    7: [Step(min(5), HR1), Step(min(35), HR2), Step(min(12), HR3)],
    8: [Step(min(5), HR1), Step(min(35), HR2), Step(min(15), HR3)],
    9: [Step(min(5), HR1), Step(min(40), HR2), Step(min(15), HR3)],
    10: [Step(min(5), HR1), Step(min(45), HR2), Step(min(15), HR3)],
}

tempo_run: dict[int, Workout] = {
    1: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Step(min(15), HR3),
        Step(min(5), HR2),
        Step(min(5), HR1),
    ],
    2: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Step(min(18), HR3),
        Step(min(5), HR2),
        Step(min(5), HR1),
    ],
    3: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Step(min(20), HR3),
        Step(min(5), HR2),
        Step(min(5), HR1),
    ],
    4: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Step(min(24), HR3),
        Step(min(5), HR2),
        Step(min(5), HR1),
    ],
    5: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Step(min(28), HR3),
        Step(min(5), HR2),
        Step(min(5), HR1),
    ],
    6: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Step(min(30), HR3),
        Step(min(5), HR2),
        Step(min(5), HR1),
    ],
    7: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Step(min(32), HR3),
        Step(min(5), HR2),
        Step(min(5), HR1),
    ],
    8: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Step(min(36), HR3),
        Step(min(5), HR2),
        Step(min(5), HR1),
    ],
    9: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Step(min(40), HR3),
        Step(min(5), HR2),
        Step(min(5), HR1),
    ],
    10: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Step(min(45), HR3),
        Step(min(5), HR2),
        Step(min(5), HR1),
    ],
}

cruise_interval_run: dict[int, Workout] = {
    1: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(4, [Step(min(5), HR3), Step(min(3), HR1)]),
        Step(min(5), HR2),
        Step(min(5), HR1),
    ],
    2: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(4, [Step(min(8), HR3), Step(min(3), HR1)]),
        Step(min(5), HR2),
        Step(min(5), HR1),
    ],
    3: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(4, [Step(min(10), HR3), Step(min(3), HR1)]),
        Step(min(5), HR2),
        Step(min(5), HR1),
    ],
    4: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(4, [Step(min(12), HR3), Step(min(3), HR1)]),
        Step(min(5), HR2),
        Step(min(5), HR1),
    ],
    5: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(4, [Step(min(15), HR3), Step(min(3), HR1)]),
        Step(min(5), HR2),
        Step(min(5), HR1),
    ],
}

long_run_with_speed_play: dict[int, Workout] = {
    1: [
        Step(mile(0.5), HR1),
        Step(mile(1), HR2),
        Repeat(8, [Step(mile(0.25), HR3), Step(mile(0.75), HR2)]),
        Step(mile(0.5), HR1),
    ],
    2: [
        Step(mile(0.5), HR1),
        Step(mile(1), HR2),
        Repeat(10, [Step(mile(0.25), HR3), Step(mile(0.75), HR2)]),
        Step(mile(0.5), HR1),
    ],
    3: [
        Step(mile(0.5), HR1),
        Step(mile(1), HR2),
        Repeat(12, [Step(mile(0.25), HR3), Step(mile(0.75), HR2)]),
        Step(mile(0.5), HR1),
    ],
    4: [
        Step(mile(0.5), HR1),
        Step(mile(1), HR2),
        Repeat(14, [Step(mile(0.25), HR3), Step(mile(0.75), HR2)]),
        Step(mile(0.5), HR1),
    ],
    5: [
        Step(mile(0.5), HR1),
        Step(mile(1), HR2),
        Repeat(16, [Step(mile(0.25), HR3), Step(mile(0.75), HR2)]),
        Step(mile(0.5), HR1),
    ],
    6: [
        Step(mile(0.5), HR1),
        Step(mile(1), HR2),
        Repeat(18, [Step(mile(0.25), HR3), Step(mile(0.75), HR2)]),
        Step(mile(0.5), HR1),
    ],
}

long_run_with_fast_finish: dict[int, Workout] = {
    1: [Step(mile(0.5), HR1), Step(mile(8.5), HR2), Step(mile(1), HR3)],
    2: [Step(mile(0.5), HR1), Step(mile(10.5), HR2), Step(mile(1), HR3)],
    3: [Step(mile(0.5), HR1), Step(mile(12), HR2), Step(mile(1), HR3)],
    4: [Step(mile(0.5), HR1), Step(mile(14), HR2), Step(mile(1), HR3)],
    5: [Step(mile(0.5), HR1), Step(mile(15.5), HR2), Step(mile(1), HR3)],
    6: [Step(mile(0.5), HR1), Step(mile(17.5), HR2), Step(mile(1), HR3)],
}

speed_play_run: dict[int, Workout] = {
    1: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(3, [Step(min(2), HR4), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    2: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(5, [Step(min(1), HR5), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    3: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(4, [Step(min(2), HR4), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    4: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(6, [Step(min(1), HR5), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    5: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(5, [Step(min(2), HR4), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    6: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(7, [Step(min(1), HR5), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    7: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(6, [Step(min(2), HR4), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    8: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(8, [Step(min(1), HR5), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    9: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(9, [Step(min(1), HR5), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    10: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(7, [Step(min(2), HR4), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    11: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(10, [Step(min(1), HR5), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    12: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(8, [Step(min(2), HR4), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    13: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(9, [Step(min(2), HR4), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    14: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(12, [Step(min(1), HR5), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
}

hill_repetition_run: dict[int, Workout] = {
    1: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(6, [Step(min(0.5), HR5, "uphill"), Step(min(1.5), HR1)]),
        Step(min(5), HR1),
    ],
    2: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(8, [Step(min(0.5), HR5, "uphill"), Step(min(1.5), HR1)]),
        Step(min(5), HR1),
    ],
    3: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(6, [Step(min(1), HR5, "uphill"), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    4: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(10, [Step(min(0.5), HR5, "uphill"), Step(min(1.5), HR1)]),
        Step(min(5), HR1),
    ],
    5: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(12, [Step(min(0.5), HR5, "uphill"), Step(min(1.5), HR1)]),
        Step(min(5), HR1),
    ],
    6: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(8, [Step(min(1), HR5, "uphill"), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    7: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(6, [Step(min(1.5), HR5, "uphill"), Step(min(2.5), HR1)]),
        Step(min(5), HR1),
    ],
    8: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(10, [Step(min(1), HR5, "uphill"), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    9: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(8, [Step(min(1.5), HR5, "uphill"), Step(min(2.5), HR1)]),
        Step(min(5), HR1),
    ],
    10: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(12, [Step(min(1), HR5, "uphill"), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    11: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(10, [Step(min(1.5), HR5, "uphill"), Step(min(2.5), HR1)]),
        Step(min(5), HR1),
    ],
    12: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(12, [Step(min(1.5), HR5, "uphill"), Step(min(2.5), HR1)]),
        Step(min(5), HR1),
    ],
}

short_interval_run: dict[int, Workout] = {
    1: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(6, [Step(min(1), HR5), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    2: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(8, [Step(min(1), HR5), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    3: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(6, [Step(min(1.5), HR5), Step(min(2.5), HR1)]),
        Step(min(5), HR1),
    ],
    4: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(10, [Step(min(1), HR5), Step(min(2.5), HR1)]),
        Step(min(5), HR1),
    ],
    5: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(8, [Step(min(1.5), HR5), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    6: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(12, [Step(min(1), HR5), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    7: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(10, [Step(min(1.5), HR5), Step(min(2.5), HR1)]),
        Step(min(5), HR1),
    ],
    8: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(12, [Step(min(1.5), HR5), Step(min(2.5), HR1)]),
        Step(min(5), HR1),
    ],
}

long_interval_run: dict[int, Workout] = {
    1: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(3, [Step(min(3), HR4), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    2: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(4, [Step(min(3), HR4), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    3: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(3, [Step(min(5), HR4), Step(min(3), HR1)]),
        Step(min(5), HR1),
    ],
    4: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(5, [Step(min(3), HR4), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    5: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(6, [Step(min(3), HR4), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    6: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(4, [Step(min(5), HR4), Step(min(3), HR1)]),
        Step(min(5), HR1),
    ],
    7: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(5, [Step(min(5), HR4), Step(min(3), HR1)]),
        Step(min(5), HR1),
    ],
    8: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(6, [Step(min(5), HR4), Step(min(3), HR1)]),
        Step(min(5), HR1),
    ],
    9: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(7, [Step(min(5), HR4), Step(min(3), HR1)]),
        Step(min(5), HR1),
    ],
    10: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(8, [Step(min(5), HR4), Step(min(3), HR1)]),
        Step(min(5), HR1),
    ],
}

mixed_interval_run: dict[int, Workout] = {
    1: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Step(min(1), HR5),
        Step(min(2), HR1),
        Step(min(3), HR4),
        Step(min(2), HR1),
        Step(min(5), HR3),
        Step(min(2), HR1),
        Step(min(3), HR4),
        Step(min(2), HR1),
        Step(min(1), HR5),
        Step(min(5), HR1),
    ],
    2: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Step(min(1.5), HR5),
        Step(min(2), HR1),
        Step(min(5), HR4),
        Step(min(2), HR1),
        Step(min(10), HR3),
        Step(min(2), HR1),
        Step(min(5), HR4),
        Step(min(2), HR1),
        Step(min(1.5), HR5),
        Step(min(5), HR1),
    ],
    3: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(2, [Step(min(1), HR5), Step(min(2), HR1)]),
        Repeat(2, [Step(min(3), HR4), Step(min(2), HR1)]),
        Step(min(10), HR3),
        Step(min(2), HR1),
        Repeat(2, [Step(min(3), HR4), Step(min(2), HR1)]),
        Repeat(2, [Step(min(1), HR5), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
    4: [
        Step(min(5), HR1),
        Step(min(5), HR2),
        Repeat(2, [Step(min(1.5), HR5), Step(min(2.5), HR1)]),
        Repeat(2, [Step(min(5), HR4), Step(min(2), HR1)]),
        Step(min(10), HR3),
        Step(min(2), HR1),
        Repeat(2, [Step(min(1.5), HR5), Step(min(2), HR1)]),
        Repeat(2, [Step(min(5), HR4), Step(min(2), HR1)]),
        Step(min(5), HR1),
    ],
}

marathon_simulator_run: Workout = [
    Step(mile(1.5), HR1),
    Step(mile(16), HR3),
    Step(mile(1), HR2),
    Step(mile(1.5), HR1),
]

runs = {
    "Recovery runs": recovery_run,
    "Foundation runs": foundation_run,
    "Long run": long_run,
    "Fast finish runs": fast_finish_run,
    "Tempo runs": tempo_run,
    "Cruise interval runs": cruise_interval_run,
    "Long runs with speed play": long_run_with_speed_play,
    "Long runs with fast finish": long_run_with_fast_finish,
    "Speed play runs": speed_play_run,
    "Hill repetition runs": hill_repetition_run,
    "Short interval runs": short_interval_run,
    "Long interval runs": long_interval_run,
    "Mixed interval runs": mixed_interval_run,
}

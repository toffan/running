from datetime import timedelta


LT = 177
"Lactate Threshold Heart Rate"


class HRZone:
    def __init__(self, number: int | None, name: str, low: float, high: float) -> None:
        self.number = number
        self.name = name
        self.low = round(low * LT)
        self.high = round(high * LT)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name!r}, {self.low!r}, {self.high!r})"

    def __str__(self) -> str:
        return f"HR[{self.low}-{self.high}]"

    def __hash__(self) -> int:
        return hash((self.number, self.name, self.low, self.high))


HR1 = HRZone(1, "Low Aerobic", 0.75, 0.80)
HR2 = HRZone(2, "Moderate Aerobic", 0.81, 0.89)
HR3 = HRZone(3, "Threshold", 0.96, 1)
HR4 = HRZone(4, "VO2 max", 1.02, 1.05)
HR5 = HRZone(5, "Speed", 1.06, 1.15)


def min(minutes: float) -> timedelta:
    return timedelta(minutes=minutes)


class distance(float):
    def __str__(self) -> str:
        return f"{self:0.1f}km"


def mile(miles: float) -> distance:
    return distance(miles * 1.61)


class Segment:
    def __init__(
        self, duration: timedelta | distance, hr: HRZone, notes: str | None = None
    ) -> None:
        self.duration = duration
        self.hr = hr
        self.notes = notes

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}({self.duration!r}, {self.hr!r}, {self.notes!r})"
        )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.duration!s} at {self.hr!s}" + (
            f", {self.notes!s})" if self.notes is not None else ")"
        )

    def __hash__(self) -> int:
        return hash((self.duration, self.hr, self.notes))


class Warmup(Segment):
    def __init__(
        self, duration: timedelta | distance = min(5), hr: HRZone = HR1
    ) -> None:
        super().__init__(duration, hr)


class Cooldown(Segment):
    def __init__(
        self, duration: timedelta | distance = min(5), hr: HRZone = HR1
    ) -> None:
        super().__init__(duration, hr)


class Recovery(Segment):
    def __init__(
        self, duration: timedelta | distance = min(2), hr: HRZone = HR1
    ) -> None:
        super().__init__(duration, hr)


class Repeat:
    def __init__(self, count: int, steps: list[Segment]) -> None:
        self.count = count
        self.steps = steps

    def __hash__(self) -> int:
        return hash((self.count, self.steps))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.count!r}, {self.steps!r})"

    def __str__(self) -> str:
        return (
            f"Rep x{self.count} [" + ", ".join(f"{step!s}" for step in self.steps) + "]"
        )


type Step = Segment | Repeat


class Workout:
    def __init__(self, steps: list[Step], name: str) -> None:
        self.steps = steps
        self.name = name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name!r}, {self.steps!r})"

    def __str__(self) -> str:
        return self.name

    def display(self) -> str:
        return f"{self.name}: " + "".join(f"\n  {step!s}" for step in self.steps)


recovery_run: dict[int, Workout] = {
    1: Workout([Segment(min(20), HR1)], name="Recovery run 1"),
    2: Workout([Segment(min(25), HR1)], name="Recovery run 2"),
    3: Workout([Segment(min(30), HR1)], name="Recovery run 3"),
    4: Workout([Segment(min(35), HR1)], name="Recovery run 4"),
    5: Workout([Segment(min(40), HR1)], name="Recovery run 5"),
    6: Workout([Segment(min(45), HR1)], name="Recovery run 6"),
    7: Workout([Segment(min(50), HR1)], name="Recovery run 7"),
    8: Workout([Segment(min(55), HR1)], name="Recovery run 8"),
    9: Workout([Segment(min(60), HR1)], name="Recovery run 9"),
}


foundation_run: dict[int, Workout] = {
    1: Workout([Warmup(), Segment(min(10), HR2), Cooldown()], name="Foundation run 1"),
    2: Workout([Warmup(), Segment(min(15), HR2), Cooldown()], name="Foundation run 2"),
    3: Workout([Warmup(), Segment(min(20), HR2), Cooldown()], name="Foundation run 3"),
    4: Workout([Warmup(), Segment(min(25), HR2), Cooldown()], name="Foundation run 4"),
    5: Workout([Warmup(), Segment(min(30), HR2), Cooldown()], name="Foundation run 5"),
    6: Workout([Warmup(), Segment(min(35), HR2), Cooldown()], name="Foundation run 6"),
    7: Workout([Warmup(), Segment(min(40), HR2), Cooldown()], name="Foundation run 7"),
    8: Workout([Warmup(), Segment(min(45), HR2), Cooldown()], name="Foundation run 8"),
    9: Workout([Warmup(), Segment(min(50), HR2), Cooldown()], name="Foundation run 9"),
}

long_run: dict[int, Workout] = {
    1: Workout(
        [Warmup(mile(1)), Segment(mile(4.5), HR2), Cooldown(mile(0.5))],
        name="Long run 1",
    ),
    2: Workout(
        [Warmup(mile(1)), Segment(mile(5.5), HR2), Cooldown(mile(0.5))],
        name="Long run 2",
    ),
    3: Workout(
        [Warmup(mile(1)), Segment(mile(6.5), HR2), Cooldown(mile(0.5))],
        name="Long run 3",
    ),
    4: Workout(
        [Warmup(mile(1)), Segment(mile(7.5), HR2), Cooldown(mile(0.5))],
        name="Long run 4",
    ),
    5: Workout(
        [Warmup(mile(1)), Segment(mile(8.5), HR2), Cooldown(mile(0.5))],
        name="Long run 5",
    ),
    6: Workout(
        [Warmup(mile(1)), Segment(mile(9.5), HR2), Cooldown(mile(0.5))],
        name="Long run 6",
    ),
    7: Workout(
        [Warmup(mile(1)), Segment(mile(10.5), HR2), Cooldown(mile(0.5))],
        name="Long run 7",
    ),
    8: Workout(
        [Warmup(mile(1)), Segment(mile(11.5), HR2), Cooldown(mile(0.5))],
        name="Long run 8",
    ),
    9: Workout(
        [Warmup(mile(1)), Segment(mile(12.5), HR2), Cooldown(mile(0.5))],
        name="Long run 9",
    ),
    10: Workout(
        [Warmup(mile(1)), Segment(mile(13.5), HR2), Cooldown(mile(0.5))],
        name="Long run 10",
    ),
    11: Workout(
        [Warmup(mile(1)), Segment(mile(14.5), HR2), Cooldown(mile(0.5))],
        name="Long run 11",
    ),
    12: Workout(
        [Warmup(mile(1)), Segment(mile(15.5), HR2), Cooldown(mile(0.5))],
        name="Long run 12",
    ),
    13: Workout(
        [Warmup(mile(1)), Segment(mile(16.5), HR2), Cooldown(mile(0.5))],
        name="Long run 13",
    ),
    14: Workout(
        [Warmup(mile(1)), Segment(mile(17.5), HR2), Cooldown(mile(0.5))],
        name="Long run 14",
    ),
    15: Workout(
        [Warmup(mile(1)), Segment(mile(18.5), HR2), Cooldown(mile(0.5))],
        name="Long run 15",
    ),
}

fast_finish_run: dict[int, Workout] = {
    1: Workout(
        [Warmup(), Segment(min(15), HR2), Segment(min(5), HR3)],
        name="Fast finish run 1",
    ),
    2: Workout(
        [Warmup(), Segment(min(20), HR2), Segment(min(5), HR3)],
        name="Fast finish run 2",
    ),
    3: Workout(
        [Warmup(), Segment(min(20), HR2), Segment(min(10), HR3)],
        name="Fast finish run 3",
    ),
    4: Workout(
        [Warmup(), Segment(min(25), HR2), Segment(min(10), HR3)],
        name="Fast finish run 4",
    ),
    5: Workout(
        [Warmup(), Segment(min(25), HR2), Segment(min(12), HR3)],
        name="Fast finish run 5",
    ),
    6: Workout(
        [Warmup(), Segment(min(30), HR2), Segment(min(12), HR3)],
        name="Fast finish run 6",
    ),
    7: Workout(
        [Warmup(), Segment(min(35), HR2), Segment(min(12), HR3)],
        name="Fast finish run 7",
    ),
    8: Workout(
        [Warmup(), Segment(min(35), HR2), Segment(min(15), HR3)],
        name="Fast finish run 8",
    ),
    9: Workout(
        [Warmup(), Segment(min(40), HR2), Segment(min(15), HR3)],
        name="Fast finish run 9",
    ),
    10: Workout(
        [Warmup(), Segment(min(45), HR2), Segment(min(15), HR3)],
        name="Fast finish run 10",
    ),
}

tempo_run: dict[int, Workout] = {
    1: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Segment(min(15), HR3),
            Segment(min(5), HR2),
            Cooldown(),
        ],
        name="Tempo run 1",
    ),
    2: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Segment(min(18), HR3),
            Segment(min(5), HR2),
            Cooldown(),
        ],
        name="Tempo run 2",
    ),
    3: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Segment(min(20), HR3),
            Segment(min(5), HR2),
            Cooldown(),
        ],
        name="Tempo run 3",
    ),
    4: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Segment(min(24), HR3),
            Segment(min(5), HR2),
            Cooldown(),
        ],
        name="Tempo run 4",
    ),
    5: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Segment(min(28), HR3),
            Segment(min(5), HR2),
            Cooldown(),
        ],
        name="Tempo run 5",
    ),
    6: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Segment(min(30), HR3),
            Segment(min(5), HR2),
            Cooldown(),
        ],
        name="Tempo run 6",
    ),
    7: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Segment(min(32), HR3),
            Segment(min(5), HR2),
            Cooldown(),
        ],
        name="Tempo run 7",
    ),
    8: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Segment(min(36), HR3),
            Segment(min(5), HR2),
            Cooldown(),
        ],
        name="Tempo run 8",
    ),
    9: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Segment(min(40), HR3),
            Segment(min(5), HR2),
            Cooldown(),
        ],
        name="Tempo run 9",
    ),
    10: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Segment(min(45), HR3),
            Segment(min(5), HR2),
            Cooldown(),
        ],
        name="Tempo run 10",
    ),
}

cruise_interval_run: dict[int, Workout] = {
    1: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(4, [Segment(min(5), HR3), Recovery(min(3))]),
            Segment(min(5), HR2),
            Cooldown(),
        ],
        name="Cruise interval run 1",
    ),
    2: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(4, [Segment(min(8), HR3), Recovery(min(3))]),
            Segment(min(5), HR2),
            Cooldown(),
        ],
        name="Cruise interval run 2",
    ),
    3: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(4, [Segment(min(10), HR3), Recovery(min(3))]),
            Segment(min(5), HR2),
            Cooldown(),
        ],
        name="Cruise interval run 3",
    ),
    4: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(4, [Segment(min(12), HR3), Recovery(min(3))]),
            Segment(min(5), HR2),
            Cooldown(),
        ],
        name="Cruise interval run 4",
    ),
    5: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(4, [Segment(min(15), HR3), Recovery(min(3))]),
            Segment(min(5), HR2),
            Cooldown(),
        ],
        name="Cruise interval run 5",
    ),
}

long_run_with_speed_play: dict[int, Workout] = {
    1: Workout(
        [
            Warmup(mile(0.5)),
            Segment(mile(1), HR2),
            Repeat(8, [Segment(mile(0.25), HR3), Segment(mile(0.75), HR2)]),
            Cooldown(mile(0.5)),
        ],
        name="Long run with speed play 1",
    ),
    2: Workout(
        [
            Warmup(mile(0.5)),
            Segment(mile(1), HR2),
            Repeat(10, [Segment(mile(0.25), HR3), Segment(mile(0.75), HR2)]),
            Cooldown(mile(0.5)),
        ],
        name="Long run with speed play 2",
    ),
    3: Workout(
        [
            Warmup(mile(0.5)),
            Segment(mile(1), HR2),
            Repeat(12, [Segment(mile(0.25), HR3), Segment(mile(0.75), HR2)]),
            Cooldown(mile(0.5)),
        ],
        name="Long run with speed play 3",
    ),
    4: Workout(
        [
            Warmup(mile(0.5)),
            Segment(mile(1), HR2),
            Repeat(14, [Segment(mile(0.25), HR3), Segment(mile(0.75), HR2)]),
            Cooldown(mile(0.5)),
        ],
        name="Long run with speed play 4",
    ),
    5: Workout(
        [
            Warmup(mile(0.5)),
            Segment(mile(1), HR2),
            Repeat(16, [Segment(mile(0.25), HR3), Segment(mile(0.75), HR2)]),
            Cooldown(mile(0.5)),
        ],
        name="Long run with speed play 5",
    ),
    6: Workout(
        [
            Warmup(mile(0.5)),
            Segment(mile(1), HR2),
            Repeat(18, [Segment(mile(0.25), HR3), Segment(mile(0.75), HR2)]),
            Cooldown(mile(0.5)),
        ],
        name="Long run with speed play 6",
    ),
}

long_run_with_fast_finish: dict[int, Workout] = {
    1: Workout(
        [Warmup(mile(0.5)), Segment(mile(8.5), HR2), Segment(mile(1), HR3)],
        name="Long run with fast finish 1",
    ),
    2: Workout(
        [Warmup(mile(0.5)), Segment(mile(10.5), HR2), Segment(mile(1), HR3)],
        name="Long run with fast finish 2",
    ),
    3: Workout(
        [Warmup(mile(0.5)), Segment(mile(12), HR2), Segment(mile(1), HR3)],
        name="Long run with fast finish 3",
    ),
    4: Workout(
        [Warmup(mile(0.5)), Segment(mile(14), HR2), Segment(mile(1), HR3)],
        name="Long run with fast finish 4",
    ),
    5: Workout(
        [Warmup(mile(0.5)), Segment(mile(15.5), HR2), Segment(mile(1), HR3)],
        name="Long run with fast finish 5",
    ),
    6: Workout(
        [Warmup(mile(0.5)), Segment(mile(17.5), HR2), Segment(mile(1), HR3)],
        name="Long run with fast finish 6",
    ),
}

speed_play_run: dict[int, Workout] = {
    1: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(3, [Segment(min(2), HR4), Recovery()]),
            Cooldown(),
        ],
        name="Speed play run 1",
    ),
    2: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(5, [Segment(min(1), HR5), Recovery()]),
            Cooldown(),
        ],
        name="Speed play run 2",
    ),
    3: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(4, [Segment(min(2), HR4), Recovery()]),
            Cooldown(),
        ],
        name="Speed play run 3",
    ),
    4: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(6, [Segment(min(1), HR5), Recovery()]),
            Cooldown(),
        ],
        name="Speed play run 4",
    ),
    5: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(5, [Segment(min(2), HR4), Recovery()]),
            Cooldown(),
        ],
        name="Speed play run 5",
    ),
    6: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(7, [Segment(min(1), HR5), Recovery()]),
            Cooldown(),
        ],
        name="Speed play run 6",
    ),
    7: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(6, [Segment(min(2), HR4), Recovery()]),
            Cooldown(),
        ],
        name="Speed play run 7",
    ),
    8: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(8, [Segment(min(1), HR5), Recovery()]),
            Cooldown(),
        ],
        name="Speed play run 8",
    ),
    9: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(9, [Segment(min(1), HR5), Recovery()]),
            Cooldown(),
        ],
        name="Speed play run 9",
    ),
    10: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(7, [Segment(min(2), HR4), Recovery()]),
            Cooldown(),
        ],
        name="Speed play run 10",
    ),
    11: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(10, [Segment(min(1), HR5), Recovery()]),
            Cooldown(),
        ],
        name="Speed play run 11",
    ),
    12: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(8, [Segment(min(2), HR4), Recovery()]),
            Cooldown(),
        ],
        name="Speed play run 12",
    ),
    13: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(9, [Segment(min(2), HR4), Recovery()]),
            Cooldown(),
        ],
        name="Speed play run 13",
    ),
    14: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(12, [Segment(min(1), HR5), Recovery()]),
            Cooldown(),
        ],
        name="Speed play run 14",
    ),
}

hill_repetition_run: dict[int, Workout] = {
    1: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(6, [Segment(min(0.5), HR5, "uphill"), Recovery(min(1.5))]),
            Cooldown(),
        ],
        name="Hill repetition run 1",
    ),
    2: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(8, [Segment(min(0.5), HR5, "uphill"), Recovery(min(1.5))]),
            Cooldown(),
        ],
        name="Hill repetition run 2",
    ),
    3: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(6, [Segment(min(1), HR5, "uphill"), Recovery(min(2))]),
            Cooldown(),
        ],
        name="Hill repetition run 3",
    ),
    4: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(10, [Segment(min(0.5), HR5, "uphill"), Recovery(min(1.5))]),
            Cooldown(),
        ],
        name="Hill repetition run 4",
    ),
    5: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(12, [Segment(min(0.5), HR5, "uphill"), Recovery(min(1.5))]),
            Cooldown(),
        ],
        name="Hill repetition run 5",
    ),
    6: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(8, [Segment(min(1), HR5, "uphill"), Recovery(min(2))]),
            Cooldown(),
        ],
        name="Hill repetition run 6",
    ),
    7: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(6, [Segment(min(1.5), HR5, "uphill"), Recovery(min(2.5))]),
            Cooldown(),
        ],
        name="Hill repetition run 7",
    ),
    8: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(10, [Segment(min(1), HR5, "uphill"), Recovery(min(2))]),
            Cooldown(),
        ],
        name="Hill repetition run 8",
    ),
    9: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(8, [Segment(min(1.5), HR5, "uphill"), Recovery(min(2.5))]),
            Cooldown(),
        ],
        name="Hill repetition run 9",
    ),
    10: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(12, [Segment(min(1), HR5, "uphill"), Recovery(min(2))]),
            Cooldown(),
        ],
        name="Hill repetition run 10",
    ),
    11: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(10, [Segment(min(1.5), HR5, "uphill"), Recovery(min(2.5))]),
            Cooldown(),
        ],
        name="Hill repetition run 11",
    ),
    12: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(12, [Segment(min(1.5), HR5, "uphill"), Recovery(min(2.5))]),
            Cooldown(),
        ],
        name="Hill repetition run 12",
    ),
}

short_interval_run: dict[int, Workout] = {
    1: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(6, [Segment(min(1), HR5), Recovery(min(2))]),
            Cooldown(),
        ],
        name="Short interval run 1",
    ),
    2: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(8, [Segment(min(1), HR5), Recovery(min(2))]),
            Cooldown(),
        ],
        name="Short interval run 2",
    ),
    3: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(6, [Segment(min(1.5), HR5), Recovery(min(2.5))]),
            Cooldown(),
        ],
        name="Short interval run 3",
    ),
    4: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(10, [Segment(min(1), HR5), Recovery(min(2.5))]),
            Cooldown(),
        ],
        name="Short interval run 4",
    ),
    5: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(8, [Segment(min(1.5), HR5), Recovery(min(2))]),
            Cooldown(),
        ],
        name="Short interval run 5",
    ),
    6: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(12, [Segment(min(1), HR5), Recovery(min(2))]),
            Cooldown(),
        ],
        name="Short interval run 6",
    ),
    7: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(10, [Segment(min(1.5), HR5), Recovery(min(2.5))]),
            Cooldown(),
        ],
        name="Short interval run 7",
    ),
    8: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(12, [Segment(min(1.5), HR5), Recovery(min(2.5))]),
            Cooldown(),
        ],
        name="Short interval run 8",
    ),
}

long_interval_run: dict[int, Workout] = {
    1: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(3, [Segment(min(3), HR4), Recovery(min(2))]),
            Cooldown(),
        ],
        name="Long interval run 1",
    ),
    2: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(4, [Segment(min(3), HR4), Recovery(min(2))]),
            Cooldown(),
        ],
        name="Long interval run 2",
    ),
    3: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(3, [Segment(min(5), HR4), Recovery(min(3))]),
            Cooldown(),
        ],
        name="Long interval run 3",
    ),
    4: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(5, [Segment(min(3), HR4), Recovery(min(2))]),
            Cooldown(),
        ],
        name="Long interval run 4",
    ),
    5: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(6, [Segment(min(3), HR4), Recovery(min(2))]),
            Cooldown(),
        ],
        name="Long interval run 5",
    ),
    6: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(4, [Segment(min(5), HR4), Recovery(min(3))]),
            Cooldown(),
        ],
        name="Long interval run 6",
    ),
    7: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(5, [Segment(min(5), HR4), Recovery(min(3))]),
            Cooldown(),
        ],
        name="Long interval run 7",
    ),
    8: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(6, [Segment(min(5), HR4), Recovery(min(3))]),
            Cooldown(),
        ],
        name="Long interval run 8",
    ),
    9: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(7, [Segment(min(5), HR4), Recovery(min(3))]),
            Cooldown(),
        ],
        name="Long interval run 9",
    ),
    10: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(8, [Segment(min(5), HR4), Recovery(min(3))]),
            Cooldown(),
        ],
        name="Long interval run 10",
    ),
}

mixed_interval_run: dict[int, Workout] = {
    1: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Segment(min(1), HR5),
            Recovery(),
            Segment(min(3), HR4),
            Recovery(),
            Segment(min(5), HR3),
            Recovery(),
            Segment(min(3), HR4),
            Recovery(),
            Segment(min(1), HR5),
            Cooldown(),
        ],
        name="Mixed interval run 1",
    ),
    2: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Segment(min(1.5), HR5),
            Recovery(),
            Segment(min(5), HR4),
            Recovery(),
            Segment(min(10), HR3),
            Recovery(),
            Segment(min(5), HR4),
            Recovery(),
            Segment(min(1.5), HR5),
            Cooldown(),
        ],
        name="Mixed interval run 2",
    ),
    3: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(2, [Segment(min(1), HR5), Recovery()]),
            Repeat(2, [Segment(min(3), HR4), Recovery()]),
            Segment(min(10), HR3),
            Recovery(),
            Repeat(2, [Segment(min(3), HR4), Recovery()]),
            Repeat(2, [Segment(min(1), HR5), Recovery()]),
            Cooldown(),
        ],
        name="Mixed interval run 3",
    ),
    4: Workout(
        [
            Warmup(),
            Segment(min(5), HR2),
            Repeat(2, [Segment(min(1.5), HR5), Recovery(min(2.5))]),
            Repeat(2, [Segment(min(5), HR4), Recovery()]),
            Segment(min(10), HR3),
            Recovery(),
            Repeat(2, [Segment(min(1.5), HR5), Recovery()]),
            Repeat(2, [Segment(min(5), HR4), Recovery()]),
            Cooldown(),
        ],
        name="Mixed interval run 4",
    ),
}

marathon_simulator_run: Workout = Workout(
    [
        Warmup(mile(1.5)),
        Segment(mile(16), HR3),
        Segment(mile(1), HR2),
        Cooldown(mile(1.5)),
    ],
    name="Marathon simulator run",
)

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

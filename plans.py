from workouts import *

half_marathon: dict[int, dict[str, list[Workout | None]]] = {
    2: {
        "W01": [
            foundation_run[5],
            fast_finish_run[3],
            foundation_run[5],
            foundation_run[5],
            speed_play_run[4],
            foundation_run[5],
            long_run[2],
        ],
        "W02": [
            foundation_run[5],
            fast_finish_run[4],
            foundation_run[6],
            foundation_run[5],
            speed_play_run[5],
            foundation_run[5],
            long_run[2],
        ],
        "W03": [
            None,
            fast_finish_run[3],
            foundation_run[5],
            foundation_run[5],
            speed_play_run[4],
            foundation_run[5],
            long_run[1],
        ],
        "W04": [
            fast_finish_run[5],
            fast_finish_run[4],
            recovery_run[6],
            foundation_run[6],
            hill_repetition_run[5],
            recovery_run[5],
            long_run[5],
        ],
        "W05": [
            foundation_run[5],
            fast_finish_run[5],
            recovery_run[6],
            foundation_run[6],
            hill_repetition_run[6],
            recovery_run[6],
            long_run[7],
        ],
        "W06": [
            None,
            fast_finish_run[4],
            recovery_run[5],
            foundation_run[5],
            hill_repetition_run[4],
            recovery_run[5],
            long_run[3],
        ],
        "W07": [
            foundation_run[6],
            cruise_interval_run[1],
            recovery_run[6],
            foundation_run[6],
            short_interval_run[4],
            recovery_run[6],
            long_run_with_speed_play[1],
        ],
        "W08": [
            recovery_run[6],
            tempo_run[4],
            recovery_run[6],
            foundation_run[6],
            short_interval_run[5],
            recovery_run[6],
            long_run_with_speed_play[2],
        ],
        "W09": [
            None,
            cruise_interval_run[1],
            recovery_run[5],
            foundation_run[6],
            short_interval_run[3],
            recovery_run[5],
            long_run_with_fast_finish[1],
        ],
        "W10": [
            foundation_run[6],
            tempo_run[5],
            recovery_run[6],
            foundation_run[6],
            long_interval_run[3],
            recovery_run[6],
            long_run_with_speed_play[2],
        ],
        "W11": [
            recovery_run[6],
            cruise_interval_run[2],
            recovery_run[6],
            foundation_run[6],
            long_interval_run[6],
            recovery_run[6],
            long_run_with_fast_finish[2],
        ],
        "W12": [
            None,
            tempo_run[4],
            recovery_run[5],
            foundation_run[6],
            long_interval_run[3],
            recovery_run[5],
            long_run_with_speed_play[1],
        ],
        "W13": [
            foundation_run[6],
            tempo_run[7],
            recovery_run[6],
            foundation_run[6],
            mixed_interval_run[2],
            recovery_run[6],
            long_run_with_fast_finish[3],
        ],
        "W14": [
            recovery_run[5],
            tempo_run[5],
            recovery_run[5],
            foundation_run[4],
            mixed_interval_run[2],
            recovery_run[4],
            long_run_with_speed_play[1],
        ],
        "W15": [
            None,
            fast_finish_run[5],
            foundation_run[4],
            foundation_run[3],
            speed_play_run[2],
            recovery_run[2],
            None,
        ],
    }
}

marathon: dict[int, dict[str, list[Workout | None]]] = {
    1: {
        "W01": [
            None,
            fast_finish_run[2],
            foundation_run[3],
            foundation_run[3],
            speed_play_run[1],
            foundation_run[3],
            long_run[1],
        ],
        "W02": [
            None,
            fast_finish_run[3],
            foundation_run[4],
            foundation_run[3],
            speed_play_run[2],
            foundation_run[3],
            long_run[2],
        ],
        "W03": [
            None,
            fast_finish_run[2],
            foundation_run[3],
            foundation_run[3],
            speed_play_run[1],
            foundation_run[3],
            long_run[1],
        ],
        "W04": [
            None,
            fast_finish_run[4],
            foundation_run[4],
            foundation_run[3],
            hill_repetition_run[1],
            recovery_run[4],
            long_run[3],
        ],
        "W05": [
            None,
            fast_finish_run[6],
            foundation_run[4],
            foundation_run[4],
            hill_repetition_run[2],
            recovery_run[4],
            long_run[4],
        ],
        "W06": [
            None,
            fast_finish_run[4],
            foundation_run[3],
            foundation_run[4],
            hill_repetition_run[1],
            recovery_run[3],
            long_run[2],
        ],
        "W07": [
            None,
            fast_finish_run[7],
            foundation_run[5],
            foundation_run[4],
            hill_repetition_run[4],
            recovery_run[4],
            long_run[5],
        ],
        "W08": [
            None,
            fast_finish_run[8],
            foundation_run[5],
            foundation_run[5],
            hill_repetition_run[6],
            recovery_run[4],
            long_run[7],
        ],
        "W09": [
            None,
            fast_finish_run[6],
            foundation_run[4],
            foundation_run[4],
            hill_repetition_run[4],
            recovery_run[4],
            long_run[4],
        ],
        "W10": [
            None,
            tempo_run[2],
            recovery_run[5],
            foundation_run[5],
            short_interval_run[1],
            recovery_run[4],
            long_run[9],
        ],
        "W11": [
            None,
            cruise_interval_run[1],
            recovery_run[5],
            foundation_run[5],
            short_interval_run[2],
            recovery_run[5],
            long_run[11],
        ],
        "W12": [
            None,
            tempo_run[2],
            recovery_run[4],
            foundation_run[5],
            short_interval_run[1],
            recovery_run[4],
            long_run_with_speed_play[1],
        ],
        "W13": [
            None,
            tempo_run[3],
            recovery_run[5],
            foundation_run[6],
            long_interval_run[2],
            recovery_run[5],
            long_run_with_fast_finish[1],
        ],
        "W14": [
            None,
            tempo_run[4],
            recovery_run[6],
            foundation_run[6],
            long_interval_run[3],
            recovery_run[5],
            long_run_with_speed_play[2],
        ],
        "W15": [
            None,
            tempo_run[2],
            recovery_run[5],
            foundation_run[5],
            long_interval_run[1],
            recovery_run[5],
            marathon_simulator_run,
        ],
        "W16": [
            None,
            cruise_interval_run[2],
            recovery_run[6],
            foundation_run[6],
            mixed_interval_run[1],
            recovery_run[6],
            long_run_with_fast_finish[5],
        ],
        "W17": [
            None,
            tempo_run[4],
            foundation_run[5],
            foundation_run[5],
            mixed_interval_run[1],
            recovery_run[4],
            long_run_with_speed_play[2],
        ],
        "W18": [
            None,
            fast_finish_run[4],
            foundation_run[4],
            foundation_run[3],
            speed_play_run[2],
            recovery_run[1],
            None,
        ],
    }
}
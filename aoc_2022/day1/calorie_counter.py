from typing import List


def convert_input_to_list(puzzle_input: str) -> List[List[int]]:
    return [
        list(map(int, section.split("\n"))) for section in puzzle_input.split("\n\n")
    ]


def calorie_counter(puzzle_input: str, top_3: bool = False) -> int:
    puzzle_list = convert_input_to_list(puzzle_input)
    calorie_leaderboard = sorted([sum(section) for section in puzzle_list])
    if top_3:
        return sum(calorie_leaderboard[-3:])
    else:
        return sum(calorie_leaderboard[-1:])

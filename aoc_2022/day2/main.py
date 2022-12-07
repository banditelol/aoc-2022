from aoc_2022.day2.puzzle_input import PUZZLE_INPUT
from aoc_2022.day2.rps_score import rps_score

if __name__ == "__main__":
    print("Day 2 - Part 1")
    print(rps_score(PUZZLE_INPUT))
    print("Day 2 - Part 2")
    print(rps_score(PUZZLE_INPUT, by_input=False))

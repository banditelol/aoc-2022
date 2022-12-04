from aoc_2022.day1.calorie_counter import calorie_counter
from aoc_2022.day1.puzzle_input import PUZZLE_INPUT

if __name__ == "__main__":
    print("Day 1 - Part 1")
    print(calorie_counter(PUZZLE_INPUT))
    print("Day 1 - Part 2")
    print(calorie_counter(PUZZLE_INPUT, top_3=True))

from typing import List, Tuple


def input_to_tuple(input_data: str) -> List[Tuple[int, int]]:
    return [
        normalize_input(tuple(line.strip().split(" ")[:2]))
        for line in input_data.split("\n")
    ]


def normalize_input(input_tuple: Tuple[str, ...]) -> Tuple[int, int]:
    assert len(input_tuple) == 2, "Input Tuple must be a pair of UPPERCASE LETTERS"
    opp, curr = input_tuple
    return ord(opp) - 64, ord(curr) - 87


def calc_by_input(opp: int, curr: int) -> int:
    score = curr
    if opp == curr:
        score += 3
    elif (
        (curr == 1 and opp == 3) or (curr == 3 and opp == 2) or (curr == 2 and opp == 1)
    ):
        score += 6
    return score


def calc_by_outcome(opp: int, curr: int) -> int:
    score = (curr - 1) * 3
    if curr == 2:
        score += opp
    elif curr == 3:
        score += (opp % 3) + 1
    else:
        if opp == 1:
            score += 3
        else:
            score += opp - 1
    return score


def rps_score(input_data: str, by_input: bool = True) -> int:
    input_tuple = input_to_tuple(input_data)
    score = 0
    calc_method = calc_by_input if by_input else calc_by_outcome
    for opp, curr in input_tuple:
        score += calc_method(opp, curr)
    return score

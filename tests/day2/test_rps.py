import pytest

from aoc_2022.day2.rps_score import rps_score


@pytest.fixture
def input_data():
    return """A Y
    B X
    C Z"""


def test_rps_running(input_data):
    rps_score(input_data)
    assert True


def test_rps_by_input(input_data):
    assert rps_score(input_data) == 15


def test_rps_by_outcome(input_data):
    assert rps_score(input_data, by_input=False) == 12

import pytest

from aoc_2022.day1.calorie_counter import calorie_counter


@pytest.fixture
def input_data():
    return """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def test_calorie_running(input_data):
    calorie_counter(input_data)
    assert True


def test_calorie_top_1(input_data):
    assert calorie_counter(input_data) == 24000


def test_calorie_top_3(input_data):
    assert calorie_counter(input_data, top_3=True) == 45000

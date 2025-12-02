import importlib


def test_day1():
    day01 = importlib.import_module("years.2025.01")

    input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

    assert day01.part1(input) == "3"
    assert day01.part2(input) == "6"

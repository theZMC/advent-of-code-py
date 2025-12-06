import importlib


def test_day03():
    day03 = importlib.import_module("years.2025.03")

    input = """987654321111111
811111111111119
234234234234278
818181911112111"""

    assert day03.part1(input) == "357"
    assert day03.part2(input) == "3121910778619"

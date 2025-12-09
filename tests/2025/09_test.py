import importlib


def test_day09():
    day09 = importlib.import_module("years.2025.09")

    input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

    assert day09.part1(input) == "50"
    assert day09.part2(input) == "24"

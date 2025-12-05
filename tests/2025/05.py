import importlib


def test_day05():
    day05 = importlib.import_module("years.2025.05")

    input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

    assert day05.part1(input) == "3"
    assert day05.part2(input) == "14"

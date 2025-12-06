import importlib


def test_day04():
    day04 = importlib.import_module("years.2025.04")

    input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

    assert day04.part1(input) == "13"
    assert day04.part2(input) == "43"

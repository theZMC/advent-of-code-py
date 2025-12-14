import importlib


def test_day12():
    day12 = importlib.import_module("years.2025.12")

    input = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

    assert day12.part1(input) == "3"  # just trust me
    assert day12.part2(input) == "Merry Christmas!"

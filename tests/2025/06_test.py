import importlib


def test_day06():
    day06 = importlib.import_module("years.2025.06")

    # fmt: off
    input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
    # fmt: on

    assert day06.part1(input) == "4277556"
    assert day06.part2(input) == "3263827"

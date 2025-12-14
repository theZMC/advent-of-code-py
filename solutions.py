from functools import reduce
from importlib import import_module
from pathlib import Path
from typing import Protocol

from questionary import select
from requests import post

SOLUTION_TEMPLATE = """def part1(input: str) -> str:
    return ""


def part2(input: str) -> str:
    return ""
"""

TEST_TEMPLATE = """import importlib


def test_day{day:02d}():
    day{day:02d} = importlib.import_module("years.{year}.{day:02d}")

    input = ""

    assert day{day:02d}.part1(input) == ""
    assert day{day:02d}.part2(input) == ""
"""


class Solution(Protocol):
    def part1(self, input: str) -> str:
        return ""

    def part2(self, input: str) -> str:
        return ""


def to_modules(year: Path) -> dict[str, Solution]:
    return reduce(
        lambda acc, day: {
            **acc,
            **{day.stem: import_module(f"years.{year.name}.{day.stem}")},
        },
        filter(lambda day: day.suffix == ".py", year.iterdir()),
        {},
    )


def gather(root="years") -> dict[str, dict[str, Solution]]:
    return reduce(
        lambda acc, year: {
            **acc,
            **{year.name: to_modules(year)},
        },
        filter(lambda p: p.is_dir(), Path(root).iterdir()),
        {},
    )


def prompt(args) -> tuple[str, str, Solution]:
    solutions = gather()
    years = [s for s in solutions.keys() if s]
    years.sort(reverse=True)  # Most recent year first
    year = (
        select(
            "Year?",
            choices=years,
        )
        .skip_if(
            len(years) == 1 or args.year, default=args.year if args.year else years[0]
        )
        .ask()
    )

    days = list(solutions[year].keys())
    days.sort(reverse=True)  # Most recent day first
    day = (
        select(
            "Day?",
            choices=days,
        )
        .skip_if(len(days) == 1 or args.day, default=args.day if args.day else days[0])
        .ask()
    )

    day = day.zfill(2)

    if not solutions[year].get(day):
        raise ValueError(f"Solution for Year {year} Day {day} not found.")

    return year, day, solutions[year][day]


def create_blank(year: str, day: str):
    if not year or not day:
        print("Please provide both --year and --day to create a new solution.")
        return

    year_path = Path("years") / year
    year_path.mkdir(parents=True, exist_ok=True)

    day_file = year_path / f"{day.zfill(2)}.py"
    if day_file.exists():
        print(f"Solution for Year {year} Day {day} already exists.")
        return

    with open(day_file, "w") as f:
        f.write(SOLUTION_TEMPLATE)

    test_path = Path("tests") / year
    test_path.mkdir(parents=True, exist_ok=True)
    test_file = test_path / f"{day.zfill(2)}_test.py"

    with open(test_file, "w") as f:
        f.write(TEST_TEMPLATE.format(day=int(day), year=int(year)))

    print(f"Created new solution template at {day_file} and a test file at {test_file}")


def submit(year: str, day: str, session: str, part1: str, part2: str):
    for i, part in enumerate([part1, part2], start=1):
        form_data = {}

        if not part:
            print(f"Part {i} answer is empty, skipping submission.")
            continue

        form_data["level"] = i
        form_data["answer"] = part
        print(f"Submitting Part {i} answer for Year {year} Day {day}...")
        print(f"Answer: \n{part}")
        choice = select("Confirm submission?", choices=["Yes", "No"]).ask()
        if choice != "Yes":
            print("Submission cancelled by user.")
            continue

        response = post(
            f"https://adventofcode.com/{year}/day/{int(day)}/answer",
            data=form_data,
            cookies={"session": session},
        )

        if response.status_code >= 200 and response.status_code < 300:
            print(f"Part {i} submitted successfully.")
        else:
            print(
                f"Failed to submit Part {i}. HTTP Status Code: {response.status_code}"
            )

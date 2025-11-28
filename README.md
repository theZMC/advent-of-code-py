# Advent of Code Python

This repository contains my solutions to the Advent of Code challenges,
implemented in Python.

The repo is structured with each year in its own directory and each day's
challenge in a separate python file. For example, the solution for Day 1 of the
year 2023 can be found in `2023/01.py` (once it's done).

## Requirements

`uv` is used to manage the project as well as its dependencies. Make sure to
install it first. You can find more information about `uv`
[here](https://uv.dev/).

## Setup

To set up the project, run the following command:

```bash
uv install
```

This will create a virtual environment and install any dependencies specified in
the `pyproject.toml` file.

## Running Solutions

To run a specific day's solution, use the following command:

```bash
uv run main.py --year <year> --day <day>
```

You can also interactively run the main script with:

```bash
uv run main.py
```

This will ask you for the year and day from the available solutions.

## Adding a new Solution

You can create a new solution file for a specific day by using the following
command:

```bash
uv run main.py --new --year <year> --day <day>
```

This will create a new Python file for the specified day in the appropriate
year's directory, pre-populated with a template.

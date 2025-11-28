from argparse import ArgumentParser, Namespace


def parse(description="Advent of Code Solver") -> Namespace:
    parser = ArgumentParser(description)
    parser.add_argument(
        "--year",
        type=str,
        help="Year of the challenge (optional)",
    )
    parser.add_argument(
        "--day",
        type=str,
        help="Day of the challenge (optional)",
    )
    parser.add_argument(
        "--session",
        type=str,
        help="Session token for fetching input (optional if .session file exists)",
    )
    parser.add_argument(
        "--session-file",
        type=str,
        help="Path to session file (optional, defaults to .session)",
    )
    parser.add_argument(
        "--new",
        action="store_true",
        help="Create a new solution template (requires --year and --day)",
    )
    parser.add_argument(
        "--submit",
        action="store_true",
        help="Submit the solutions automatically (will skip empty solutions)",
    )
    return parser.parse_args()

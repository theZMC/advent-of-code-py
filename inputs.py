from requests import get


def fetch(year: str, day: str, session: str) -> str:
    resp = get(
        f"https://adventofcode.com/{year}/day/{int(day)}/input",  # int(day) to remove leading zeros
        cookies={"session": session},
    )

    if resp.status_code != 200:
        raise Exception(
            f"Failed to fetch input for {year} Day {int(day)}. HTTP Status Code: {resp.status_code}"
        )

    return resp.text

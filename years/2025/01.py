from functools import reduce


def accumulate_zero_hits(acc: tuple[int, int], line: str):
    count, cur = acc

    coef = -1 if line[0] == "L" else 1

    dist = int(line[1:])
    new = cur + (dist * coef)

    while new > 99:
        new = new - 100

    while new < 0:
        new = new + 100

    if new == 0:
        count += 1

    return count, new


def accumulate_zero_crossings(acc: tuple[int, int], line: str):
    count, cur = acc
    coef = -1 if line[0] == "L" else 1

    dist = int(line[1:])
    new = cur
    for _ in range(dist):
        new = (new + coef) % 100
        if new == 0:
            count += 1

    return count, new


def part1(input: str) -> str:
    count, _ = reduce(accumulate_zero_hits, input.splitlines(), (0, 50))
    return str(count)


def part2(input: str) -> str:
    count, _ = reduce(accumulate_zero_crossings, input.splitlines(), (0, 50))
    return str(count)

from functools import reduce
from itertools import batched
from operator import add


def to_invalid_ids_part1(id_range: str):
    bounds = id_range.split("-")
    id_start = bounds[0]
    id_end = bounds[1]

    ids = range(int(id_start), int(id_end) + 1)
    invalid_ids = []
    for id in [str(id) for id in ids]:
        id_len = len(id)

        if id_len % 2 != 0:
            continue

        h1 = id[: id_len // 2]
        h2 = id[id_len // 2 :]

        if h1 == h2:
            invalid_ids.append(id)

    return invalid_ids


def part1(input: str) -> str:
    invalid_ids = reduce(add, map(to_invalid_ids_part1, input.split(",")))
    return str(sum([int(i) for i in invalid_ids]))


def to_invalid_ids_part2(id_range: str):
    bounds = id_range.split("-")
    id_start = bounds[0]
    id_end = bounds[1]

    ids = [str(id) for id in range(int(id_start), int(id_end) + 1)]
    invalid_ids = []
    for id in ids:
        id_len = len(id)

        for i in range(1, (id_len // 2) + 1):
            batches = batched(list(id), i)
            first = next(batches)

            if all(b == first for b in batches):
                invalid_ids.append(id)
                break

    return invalid_ids


def part2(input: str) -> str:
    invalid_ids = reduce(add, map(to_invalid_ids_part2, input.split(",")))
    return str(sum([int(i) for i in invalid_ids]))

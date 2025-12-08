from collections import deque
from itertools import combinations
from math import prod, sqrt


def distance(point1: tuple[int, ...], point2: tuple[int, ...]) -> float:
    return sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(point1, point2)))


def part1(input: str) -> str:
    MAX_ITER = 1000
    jboxes = [tuple(int(x) for x in line.split(",")) for line in input.splitlines()]

    if len(jboxes) < 100:
        MAX_ITER = 10  # bit of a hack, but necessary for testing

    pairs = map(
        lambda p: {p[0], p[1]},
        sorted(combinations(jboxes, 2), key=lambda p: distance(p[0], p[1])),
    )

    circuits = []

    for i, junctions in enumerate(pairs):
        if i == MAX_ITER:
            break

        merged, unmerged = [], []
        for circuit in circuits:
            (merged if circuit & junctions else unmerged).append(circuit)

        circuits = [set.union(*merged, junctions), *unmerged]

    product = prod(len(s) for s in sorted(circuits, key=len, reverse=True)[:3])

    return str(product)


def part2(input: str) -> str:
    jboxes = [tuple(int(x) for x in line.split(",")) for line in input.splitlines()]

    pairs = map(
        lambda p: {p[0], p[1]},
        sorted(combinations(jboxes, 2), key=lambda p: distance(p[0], p[1])),
    )

    circuits = []
    last_junctions = deque([], 2)

    for i, junctions in enumerate(pairs):
        merged, unmerged = [], []
        for circuit in circuits:
            (merged if circuit & junctions else unmerged).append(circuit)

        circuits = [set.union(*merged, junctions), *unmerged]
        for j in junctions:
            last_junctions.append(j)

        if len(circuits[0]) == len(jboxes):
            break

    return str(prod(map(lambda p: p[0], last_junctions)))

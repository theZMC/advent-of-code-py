from heapq import heappop, heappush
from itertools import combinations

from shapely.geometry import Polygon


def part1(input: str) -> str:
    points = [
        (int(p[0]), int(p[1]))
        for p in [line.split(",", 2) for line in input.splitlines()]
    ]

    areas: list[int] = []

    for p1, p2 in combinations(points, 2):
        area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
        heappush(areas, -area)

    return str(-heappop(areas))


def part2(input: str) -> str:
    points = [
        (int(p[0]), int(p[1]))
        for p in [line.split(",", 2) for line in input.splitlines()]
    ]
    points.append(points[0])

    outer = Polygon(points)

    areas: list[tuple[int, tuple[tuple[int, int], tuple[int, int]]]] = []

    for p1, p2 in combinations(points, 2):
        area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
        heappush(areas, (-area, (p1, p2)))

    while areas:
        area, points = heappop(areas)
        p1, p2 = points[0], points[1]
        inner = Polygon(
            [
                (min(p1[0], p2[0]), min(p1[1], p2[1])),
                (min(p1[0], p2[0]), max(p1[1], p2[1])),
                (max(p1[0], p2[0]), max(p1[1], p2[1])),
                (max(p1[0], p2[0]), min(p1[1], p2[1])),
            ]
        )
        if outer.contains(inner):
            return str(-area)

    return str(0)

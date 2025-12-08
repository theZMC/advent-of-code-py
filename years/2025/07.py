from functools import cache


def find_start_and_splitters(grid: list[list[str]]):
    splitter_coords: list[tuple[int, int]] = []

    start: tuple[int, int]
    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            if grid[x][y] == "^":
                splitter_coords.append((x, y))
            if grid[x][y] == "S":
                start = (x, y)

    return start, splitter_coords


def part1(input: str) -> str:
    grid = [list(line) for line in input.splitlines()]

    start, splitters = find_start_and_splitters(grid)

    visited = set([])

    def recurse(start, coords):
        sx, sy = start[0], start[1]
        if sx < 0 or sy < 0 or sx >= len(grid) or sy >= len(grid[0]):
            return 0

        for coord in coords:
            cx, cy = coord[0], coord[1]

            if sy == cy and cx > sx:
                if (cx, cy) in visited:
                    break

                visited.add((cx, cy))

                left = (cx, cy - 1)
                right = (cx, cy + 1)
                return recurse(left, coords) + recurse(right, coords)

        return 1

    total = recurse(start, splitters) - 1

    return str(total)


def part2(input: str) -> str:
    grid = [list(line) for line in input.splitlines()]

    start, splitters = find_start_and_splitters(grid)

    @cache
    def recurse(start, coords):
        sx, sy = start[0], start[1]
        if sx < 0 or sy < 0 or sx >= len(grid) or sy >= len(grid[0]):
            return 0

        for coord in coords:
            cx, cy = coord[0], coord[1]

            if sy == cy and cx > sx:
                left = (cx, cy - 1)
                right = (cx, cy + 1)
                return recurse(left, coords) + recurse(right, coords)

        return 1

    total = recurse(start, tuple(splitters))

    return str(total)

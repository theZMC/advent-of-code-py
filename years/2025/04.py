def count_adjacent(x: int, y: int, grid: list[list[str]]):
    search_grid = [(sx, sy) for sx in range(-1, 2) for sy in range(-1, 2)]

    count = 0
    for sx, sy in [(x + dx, y + dy) for (dx, dy) in search_grid]:
        if (sx, sy) == (x, y):
            continue
        if sx < 0 or sy < 0 or sx >= len(grid) or sy >= len(grid[sx]):
            continue
        if grid[sx][sy] == "@":
            count += 1

    return count


def part1(input: str) -> str:
    grid = []

    for x in input.splitlines():
        grid.append(list(x))

    total = 0
    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            if grid[x][y] != "@":
                continue
            adjacent_count = count_adjacent(x, y, grid)
            if adjacent_count < 4:
                total += 1

    return str(total)


def part2(input: str) -> str:
    grid = []

    for x in input.splitlines():
        grid.append(list(x))

    def recurse(grid: list[list[str]]) -> int:
        next_grid = []
        total = 0
        for x in range(0, len(grid)):
            next_grid.append(grid[x])
            for y in range(0, len(grid[x])):
                if grid[x][y] != "@":
                    continue
                adjacent_count = count_adjacent(x, y, grid)
                if adjacent_count < 4:
                    next_grid[x][y] = "."
                    total += 1

        if total == 0:
            return 0
        return total + recurse(grid)

    return str(recurse(grid))

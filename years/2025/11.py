from functools import cache


def len_all_paths_part1(graph: dict[str, set[str]], start: str, end: str) -> int:
    @cache
    def dfs(next: str) -> int:
        if next == end:
            return 1
        if (children := graph.get(next)) is None:
            return 0
        return sum(dfs(child) for child in children)

    return dfs(start)


def part1(input: str) -> str:
    graph: dict[str, set[str]] = dict()
    for line in input.splitlines():
        key, value = line.split(": ", 1)
        graph[key] = set(value.split())

    return str(len_all_paths_part1(graph, "you", "out"))


def len_all_paths_part2(graph: dict[str, set[str]], start: str, end: str) -> int:
    @cache
    def dfs(next: str, found_fft: bool, found_dac: bool) -> int:
        if next == end:
            return 1 if found_fft and found_dac else 0
        if (children := graph.get(next)) is None:
            return 0
        if next == "fft":
            found_fft = True
        if next == "dac":
            found_dac = True
        return sum(dfs(child, found_fft, found_dac) for child in children)

    return dfs(start, False, False)


def part2(input: str) -> str:
    graph = {}
    for line in input.splitlines():
        key, value = line.split(": ", 1)
        graph[key] = set(value.split())

    return str(len_all_paths_part2(graph, "svr", "out"))

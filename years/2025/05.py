def part1(input: str) -> str:
    parts = input.split("\n\n")
    ranges = parts[0]
    ingredients = parts[1]

    fresh_ranges = []

    for fresh_range in ranges.splitlines():
        parts = fresh_range.split("-")
        start = parts[0]
        end = parts[1]
        fresh_ranges.append((int(start), int(end)))

    fresh_count = 0

    for ingredient in [int(ingredient) for ingredient in ingredients.splitlines()]:
        for fresh_range in fresh_ranges:
            if fresh_range[0] <= ingredient <= fresh_range[1]:
                fresh_count += 1
                break

    return str(fresh_count)


def part2(input: str) -> str:
    parts = input.split("\n\n")
    ranges = parts[0]

    total = 0
    fresh_ranges = []

    for fresh_range in ranges.splitlines():
        parts = fresh_range.split("-")
        start = parts[0]
        end = parts[1]
        fresh_ranges.append([int(start), int(end)])

    fresh_ranges.sort()
    merged_ranges = []

    for start, end in fresh_ranges:
        if not merged_ranges or start > merged_ranges[-1][1]:
            merged_ranges.append([start, end])
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)

    total = 0
    for start, end in merged_ranges:
        total += end - start + 1

    return str(total)

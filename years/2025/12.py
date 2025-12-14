def part1(input: str) -> str:
    presents, requirements = requirements_from_input(input)
    possible_count = 0
    for area, present_counts in requirements:
        used_area = 0
        for i, count in enumerate(present_counts):
            used_area += count * presents[i]
        if used_area <= area:
            possible_count += 1

    return str(possible_count)


def requirements_from_input(
    input: str,
) -> tuple[list[int], list[tuple[int, list[int]]]]:
    presents_and_places = input.split("\n\n")

    presents = presents_and_places[:-1]
    places = presents_and_places[-1]

    sizes = []

    for present in presents:
        lines = present.splitlines()
        size = 0
        for line in lines[1:]:
            for char in list(line):
                if char == "#":
                    size += 1

        sizes.append(size)

    requirements: list[tuple[int, list[int]]] = []
    for place in places.splitlines():
        parts = place.split()
        dimensions = parts[0].split(":")[0]
        sides = dimensions.split("x")
        area = int(sides[0]) * int(sides[1])
        requirements.append((area, list(map(int, parts[1:]))))

    return (sizes, requirements)


def part2(_: str) -> str:
    return "Merry Christmas!"

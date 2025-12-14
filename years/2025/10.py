from collections import defaultdict
from itertools import combinations

from z3 import z3


def find_min_presses(target: int, presses: list[list[int]]) -> tuple[list[int], ...]:
    for i in range(len(presses)):
        for combo in combinations(presses, i):
            switch_state = 0
            for toggles in combo:
                mask = 0
                for t in toggles:
                    mask ^= 1 << t
                switch_state ^= mask
            if switch_state == target:
                return combo

    return tuple()


def part1(input: str) -> str:
    machines = parse_machines(input)
    press_count = sum([len(find_min_presses(m[0], m[1])) for m in machines])

    return str(press_count)


def parse_machines(
    input: str,
) -> list[tuple[int, list[list[int]], list[int]]]:
    machine_configs = input.splitlines()

    machines: list[tuple[int, list[list[int]], list[int]]] = []

    for machine_config in machine_configs:
        machine_and_rest = machine_config.split(maxsplit=1)

        target_chars = list(machine_and_rest[0])[1:-1]
        presses_chars = " ".join(machine_and_rest[1].split()[:-1]).split()
        joltage_chars = machine_and_rest[1].split()[-1]

        target = 0
        for i, ch in enumerate(target_chars):
            if ch == "#":
                target |= 1 << i

        presses = [[int(n) for n in g[1:-1].split(",")] for g in presses_chars]

        joltages = [int(j) for j in joltage_chars[1:-1].split(",")]

        machines.append((target, presses, joltages))

    return machines


def press_buttons(machine: int, presses: list[int]) -> int:
    for complement in presses:
        machine ^= 1 << machine

    return machine


def part2(input: str) -> str:
    machines = parse_machines(input)
    total = 0
    for _, presses, joltages in machines:
        solver = z3.Optimize()
        z3presses = z3.IntVector("p", len(presses))

        press_indices = defaultdict(list)
        for i, press in enumerate(presses):
            for p in press:
                press_indices[int(p)].append(i)
            solver.add(z3presses[i] >= 0)

        for i, indices in press_indices.items():
            solver.add(joltages[i] == sum(z3presses[i] for i in indices))

        presses = z3.Sum(z3presses)
        solver.minimize(presses)
        solver.check()

        result = solver.model().eval(presses)
        assert isinstance(result, z3.IntNumRef)
        total += result.as_long()

    return str(total)

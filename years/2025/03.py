def part1(input: str) -> str:
    banks = input.splitlines()
    joltage = []
    for bank in banks:
        first = "0"
        second = "0"

        for pos, battery in enumerate(list(bank)):
            if battery > first and pos != len(bank) - 1:
                first = battery
                second = "0"
                continue

            if battery > second:
                second = battery

        joltage.append(str(first) + str(second))

    return str(sum([int(v) for v in joltage]))


def part2(input: str) -> str:
    banks = input.splitlines()
    joltages = []

    for bank in banks:
        position = 0
        bank_len = len(bank)
        joltage = []

        for remaining in range(12, 0, -1):
            end = bank_len - remaining + 1
            highest = max(bank[position:end])
            position = bank.index(highest, position, end) + 1
            joltage.append(highest)

        joltages.append("".join(joltage))

    return str(sum([int(joltage) for joltage in joltages]))

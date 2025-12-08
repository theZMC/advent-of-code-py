def part1(input: str) -> str:
    problems = input.splitlines()
    problems.reverse()

    operators = problems[0].split()

    total = 0
    for i, operator in enumerate(operators):
        operation_total = 0
        if operator == "*":
            operation_total = 1

        for line in [line.split() for line in problems[1:]]:
            if operator == "*":
                operation_total *= int(line[i])
            if operator == "+":
                operation_total += int(line[i])

        total += operation_total

    return str(total)


def part2(input: str) -> str:
    lines = input.splitlines()
    operators = lines[-1].split()

    lines = [
        " " + line for line in lines[:-1]
    ]  # make sure the "last" column is all spaces

    total = 0

    factors = []

    indexes = list(range(0, len(lines[0])))
    indexes.reverse()

    for i in indexes:
        factor_digits = []

        for line in lines:
            digit = line[i]
            if digit == " ":
                continue
            factor_digits.append(digit)

        if factor_digits:
            factors.append(int("".join(factor_digits)))
            continue

        operator = operators.pop()

        operation_total = 0

        if operator == "*":
            operation_total = 1

        for factor in factors:
            if operator == "*":
                operation_total *= int(factor)
            if operator == "+":
                operation_total += int(factor)

        factors = []  # reset the factors

        total += operation_total

    return str(total)

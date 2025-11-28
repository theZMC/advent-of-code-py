import arguments
import inputs
import sessions
import solutions


def main():
    args = arguments.parse()
    if args.new:
        return solutions.create_blank(args.year, args.day)

    session = sessions.get(args)

    year, day, solution = solutions.prompt(args)

    input = inputs.fetch(year, day, session)

    print(f"Year {year} Day {day} Solutions:")

    part1 = solution.part1(input)
    print(f"Part 1: \n{part1}")

    part2 = solution.part2(input)
    print(f"Part 2: \n{part2}")

    if args.submit:
        solutions.submit(year, day, session, part1, part2)


if __name__ == "__main__":
    main()

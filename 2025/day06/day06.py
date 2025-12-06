import re

def part1(math_homework: str) -> None:
    problems = {}

    reg = re.compile(r'(\d+|\+|\*)')


    for line in math_homework.split('\n'):
        if not line:
            break

        for idx, pos in enumerate(reg.findall(line)):
            if not idx in problems:
                problems[idx] = []

            problems[idx].append(pos)


    homework_total = 0
    for problem in problems.values():
        problem_total = int(problem[0])

        operator = problem[-1]
        for i in [int(x) for x in problem[1:-1]]:
            if operator == '*':
                problem_total = problem_total * i
            elif operator == '+':
                problem_total = problem_total + i
            else:
                print(f"ERROR: Unsupported operator {operator}")

        #print(problem, problem_total)
        homework_total += problem_total


    print(f"Part 1: {homework_total}")


if __name__ == '__main__':
    with open('input.txt', encoding="utf-8") as file:
        puzzle_input = file.read()
    part1(puzzle_input)

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

    homework_total = solve_and_total_all_problems(problems)
    print(f"Part 1: {homework_total}")


def solve_and_total_all_problems(problems: dict[int, list]) -> int:
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
    return homework_total



def part2(math_homework: str) -> None:
    """
    Going to stick the whole thing in a grid.
    Then we're going to go through the grid RIGHT to LEFT. We know we get to a
    problem boundary if we find an operator character. We just ignore the blank
    columns.
    After building a problems dictionary, we will solve it just like in part 1.
    """
    grid = {}
    for y, line in enumerate(math_homework.split('\n')):
        for x, val in enumerate(line):
            grid[(x, y)] = val

    problems = {}
    problem_counter = 0

    max_x = max([x[0] for x in grid])
    max_y = max([y[1] for y in grid])

    x = max_x
    while x >=0:
        number = ''
        operator = None
        for y in range(max_y+1):
            if (x, y) in grid:
                val = grid[(x, y)]

                if val == '*' or val == '+':
                    operator = val
                else:
                    #print(grid[(x, y)])
                    number += val


        #print(f"== {number} ==")
        if not problem_counter in problems:
            problems[problem_counter] = []
        try:
            problems[problem_counter].append(int(number))
        except:
            # this is for the blank "lines"
            pass

        if operator:
            problems[problem_counter].append(operator)
            problem_counter += 1


        x = x - 1


    homework_total = solve_and_total_all_problems(problems)
    print(f"Part 2: {homework_total}")


if __name__ == '__main__':
    with open('input.txt', encoding="utf-8") as file:
        puzzle_input = file.read()
    part1(puzzle_input)
    part2(puzzle_input)

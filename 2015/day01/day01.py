with open('input') as file:
    input_str = file.read()


def part1(input_str):
    floor = 0

    for instruction in input_str:
        if instruction == '(':
            floor += 1

        if instruction == ')':
            floor -= 1

    print(f"Part 1: {floor}")

    return True

def part2(input_str):
    floor = 0
    for i in range(len(input_str)):
        if input_str[i] == '(':
            floor += 1

        if input_str[i] == ')':
            floor -= 1

        if floor == -1:
            print(f"Part 2: {i + 1}")
            break

    return True

part1(input_str)
part2(input_str)

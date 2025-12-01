def part1(puzzle_lines: list) -> int:
    zero_counter = 0
    dial = 50
    for instruction in puzzle_lines:
        if instruction[0] == 'L':
            new_dial = ( dial - int(instruction[1:]) ) % 100

        elif instruction[0] == 'R':
            new_dial = dial + int(instruction[1:])

        else:
            print("ERROR: Instructions should only contain L or R")
            return -1

        dial = int(str(new_dial)[-2:])
#        print(f"{instruction}: {dial}")

        if dial == 0:
            zero_counter += 1

    return zero_counter

def part2(puzzle_lines: list) -> int:
    zero_counter = 0
    dial = 50
    for instruction in puzzle_lines:
        new_zeroes = 0
        if instruction[0] == 'L':
            new_dial = dial - int(instruction[1:])
            if new_dial <= 0:
                if dial == 0:
                    new_zeroes = abs(int(new_dial / 100))
                else:
                    new_zeroes = abs(int(new_dial / 100)) + 1
#                if zero_counter > 0:
#                    print(f"new_dial {new_dial}: new_zeroes {new_zeroes}")

            new_dial = new_dial % 100

        elif instruction[0] == 'R':
            new_dial = dial + int(instruction[1:])
            if new_dial >= 100:
                new_zeroes = int(new_dial / 100)
#                if zero_counter > 0:
#                    print(f"new_dial {new_dial}: new_zeroes {new_zeroes}")

        else:
            print("ERROR: Instructions should only contain L or R")
            return -1

        dial = int(str(new_dial)[-2:])
#        print(f"{instruction}: {dial}")

        zero_counter += new_zeroes

#        print(f"instruction: {instruction}, dial: {dial}, zero_counter: {zero_counter}")

    return zero_counter

if __name__ == '__main__':
    with open('input.txt') as file:
        puzzle_lines = file.read().splitlines()
    print(part1(puzzle_lines))
    print(part2(puzzle_lines))

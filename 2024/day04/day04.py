with open('input.txt') as file:
    puzzle_lines = file.readlines()

def check_direction(grid: list, y: int, x: int, direction: str, target: str = 'M', part: int = 1) -> bool:
    # Cardinal directions.
    # Modify our coordinates to check the direction.
    # Safety checks to avoid out of bounds.
    if direction == 'n':
        if y == 0:
            return False
        y -= 1
    elif direction == 'ne':
        if y == 0 or x == len(grid[0])-1:
            return False
        y -= 1
        x += 1
    elif direction == 'e':
        if x == len(grid[0])-1:
            return False
        x += 1
    elif direction == 'se':
        if y == len(grid)-1 or x == len(grid[0])-1:
            return False
        y += 1
        x += 1
    elif direction == 's':
        if y == len(grid)-1:
            return False
        y += 1
    elif direction == 's':
        if y == len(grid)-1:
            return False
        y += 1
    elif direction == 'sw':
        if y == len(grid)-1 or x == 0:
            return False
        y += 1
        x -= 1
    elif direction == 'w':
        if x == 0:
            return False
        x -= 1
    elif direction == 'nw':
        if y == 0 or x == 0:
            return False
        y -= 1
        x -= 1
    else:
        print(f"Direction is weird: {direction}")
        return False


#    print(f"{y} {x}")
    if part == 1:
        if grid[y][x] == target:
    #        print(f"Found target {target} at {y}, {x}")
            if target == 'M':
                next_target = 'A'
            elif target == 'A':
                next_target = 'S'
            elif target == 'S':
                return True
            else:
                print(f"Next Target can't be set. Current target is: {target}")
                return False

            return check_direction(grid, y, x, direction, next_target)
    elif part == 2:
        if grid[y][x] == target:
            return True

    return False

def part1(puzzle_lines: list) -> bool:
    # Get input into a 2d array
    grid = []
    for i in range(len(puzzle_lines)):
        grid.append(list(puzzle_lines[i].strip()))

#    for line in grid:
#        print(line)

    directions = ['n',
                  'nw',
                  'w',
                  'sw',
                  's',
                  'se',
                  'e',
                  'ne']

    words_found = 0

    # We'll start by looking for X's
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'X':
#                print(f"Found an X at: {y}, {x}")
                for direction in directions:
                    if check_direction(grid, y, x, direction):
#                        print(f"Found XMAS at: {y}, {x} going {direction}")
                        words_found += 1


    print(f"Part 1: {words_found}")
    return True

def part2(puzzle_lines: list) -> bool:
    # Get input into a 2d array
    grid = []
    for i in range(len(puzzle_lines)):
        grid.append(list(puzzle_lines[i].strip()))

    words_found = 0

    # We'll start by looking for A's
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'A':
                backwards_found = False
                forwards_found = False

#                print(f"Found an A at: {y}, {x}")
                if check_direction(grid, y, x, 'nw', 'M', part=2):
                    if check_direction(grid, y, x, 'se', 'S', part=2):
                        backwards_found = True
                if check_direction(grid, y, x, 'nw', 'S', part=2):
                    if check_direction(grid, y, x, 'se', 'M', part=2):
                        backwards_found = True
                if check_direction(grid, y, x, 'ne', 'M', part=2):
                    if check_direction(grid, y, x, 'sw', 'S', part=2):
                        forwards_found = True
                if check_direction(grid, y, x, 'ne', 'S', part=2):
                    if check_direction(grid, y, x, 'sw', 'M', part=2):
                        forwards_found = True

                if backwards_found and forwards_found:
                    words_found += 1


    print(f"Part 2: {words_found}")
    return True

part1(puzzle_lines)
part2(puzzle_lines)

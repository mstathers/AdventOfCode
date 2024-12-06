with open('input.txt') as file:
    grid = []
    for puzzle_lines in file.readlines():
        grid.append(list(puzzle_lines.strip()))

def part1(grid):
    # find starting position
    facing, y, x = find_guard(grid)
    if facing == 'na':
        print("Guard not found")
        return False

    # save starting location as visited in set
    visited = {f"{y},{x}"}

    while (facing != 'na'):
        facing, y, x = check_next_location(grid, facing, y, x)
        visited.add(f"{y},{x}")

    print(f"Part 1: {len(visited)}")
    return True

def find_guard(grid: list[list])-> tuple[str, int, int]:
    guard_facings = ['^', '>', 'v', '<']
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in guard_facings:
                facing = str(grid[y][x])
                return facing, y, x
    return 'na', 0, 0

def check_next_location(grid: list[list], facing: str, y: int, x: int) -> tuple[str, int, int]:
    orig_x = x
    orig_y = y
    # Get next grid location.
    # Break out if we go off map
    if facing == '^':
        if y == 0:
            return 'na', orig_y, orig_x
        y -= 1
    elif facing == '>':
        if x == len(grid[0])-1:
            return 'na', orig_y, orig_x
        x += 1
    elif facing == 'v':
        if y == len(grid)-1:
            return 'na', orig_y, orig_x
        y += 1
    elif facing == '<':
        if x == 0:
            return 'na', orig_y, orig_x
        x -= 1

    # Check ahead of guard
    # Turn 90deg right if obstacle
    # Recursion to check that new direction
    if grid[y][x] == '#':
        guard_facings = ['^', '>', 'v', '<']
        try:
            facing = guard_facings[guard_facings.index(facing) + 1]
        except IndexError:
            facing = guard_facings[0]

        # Check next direction
        return check_next_location(grid, facing, orig_y, orig_x)

    return facing, y, x


part1(grid)

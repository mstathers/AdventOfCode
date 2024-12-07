with open('input.txt') as file:
    grid = []
    for puzzle_lines in file.readlines():
        grid.append(list(puzzle_lines.strip()))

def part1(grid: list[list]):
    # find starting position
    facing, y, x = find_guard(grid)
    if facing == 'na':
        print("Guard not found")
        return []

    # save starting location as visited in set
    visited = {f"{y},{x}"}

    while (facing != 'na'):
        facing, y, x = check_next_location(grid, facing, y, x)
        visited.add(f"{y},{x}")

    #print(f"Part 1: {len(visited)}")
    return visited

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

# We'll get our visited guard locations from part1 as we only need to check
# those.
def part2(grid, visited):
    looping_obstructions = 0

    # Make a nice array of valid guard locations from part1
    guard_locations = []
    for location in visited:
        guard_locations.append(location.split(','))

    # find guard starting position
    orig_facing, orig_y, orig_x = find_guard(grid)
    if orig_facing == 'na':
        print("Guard not found")
        return []

    # We're going to place an obstacle at each potential guard location.
    for g_loc in guard_locations:
        obs_y = int(g_loc[0])
        obs_x = int(g_loc[1])

        # We can't put an obstacle where the guard begins.
        if orig_y == obs_y and orig_x == obs_x:
            continue

        # Place obstacle on the grid.
        grid[obs_y][obs_x] = '#'

        # For each  test we'll save our location and facing. We can use this
        # later to check if we've been here. Format:
        # [f"{facing},{y},{x}"]
        visited = []

        # Need to reset these for every test.
        facing = orig_facing
        x = orig_x
        y = orig_y

        # stop if we go off the board, or if we have already been here.
        while (facing != 'na') and (f"{facing},{y},{x}" not in visited):
            visited.append(f"{facing},{y},{x}")
            facing, y, x = check_next_location(grid, facing, y, x)

        if f"{facing},{y},{x}" in visited:
            looping_obstructions += 1

        # Remove our obstacle for the next test.
        grid[obs_y][obs_x] = '.'


    print(f"Part 2: {looping_obstructions}")
    return True


print(f"Part 1: {len(part1(grid))}")
part2(grid, part1(grid))

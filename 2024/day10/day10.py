with open('test-input.txt', 'r', encoding='utf8') as file:
    grid = []
    for puzzle_line in file.readlines():
        grid.append(list([int(x) for x in puzzle_line.strip()]))

def part1(grid: list[list[int]]):
    valid_trails = 0
    trailheads = find_trailheads(grid)

    for trailhead in trailheads:
        print(trailhead)

        valid_trails += valid_trails_from_loc(grid, trailhead)

        break # XXX

    print(f"Part 1: {valid_trails}")
    return True

def find_trailheads(grid: list[list[int]]) -> set[tuple[int, int]]:
    """
    Find all trailheads (value == 0) on the grid, return a set of coordinate
    tuples.
    """
    t_heads = set()
    for y_idx, y in enumerate(grid):
        for x_idx, x in enumerate(y):
            if x == 0:
                t_heads.add((y_idx, x_idx))

    return t_heads

def bounds_check(grid: list[list[int]], y: int, x: int) -> bool:
    # set limits based on size of grid:
    max_depth = len(grid)-1
    max_width = len(grid[0])-1

    if (0 <= y <= max_depth and
        0 <= x <= max_width):
        return True
    return False

def valid_trails_from_loc(grid: list[list[int]], loc: tuple[int, int], elevation: int = 0, valid_trails: int = 0) -> int:
    y, x = loc

    for direction in ['n', 'e', 's', 'w']:
        if direction == 'n':
            new_y = y - 1
            new_x = x
        elif direction == 'e':
            new_y = y
            new_x = x + 1
        elif direction == 's':
            new_y = y + 1
            new_x = x
        elif direction == 'w':
            new_y = y
            new_x = x - 1
        # We shouldn't ever get here
        else:
            new_y = -1
            new_x = -1

        print(f"{loc} checking {direction} for {elevation + 1}")


        if not bounds_check(grid, new_y, new_x):
            print(f"Out of Bounds: {(new_y, new_x)}")
            continue


        if grid[new_y][new_x] == elevation + 1:
            if grid[new_y][new_x] == 2:
                print(f"Found peak: {(new_y, new_x)} going {direction}, valid_trails: {valid_trails}")
                valid_trails += 1

            else:
                print(f"coords: {(new_y, new_x)}, elevation: {elevation}, direction: {direction}, valid_trails: {valid_trails}")
                #XXX check if we've been here already and can re-use the value for number of valid trails
                #return valid_trails_from_loc(grid, (new_y, new_x), elevation + 1, valid_trails)
                valid_trails += valid_trails_from_loc(grid, (new_y, new_x), elevation + 1, valid_trails)

    return valid_trails


part1(grid)

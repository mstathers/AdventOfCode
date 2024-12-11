import time

TOTAL_TRAILS = 0

def timer(func):
    def wrapper(*arg):
        start_t = time.perf_counter()
        res = func(*arg)
        end_t = time.perf_counter()
        elapsed_t = end_t - start_t
        print(f"Time taken: {elapsed_t:.6f} seconds")
        return res
    return wrapper


with open('input.txt', 'r', encoding='utf8') as file:
    grid = []
    for puzzle_line in file.readlines():
        grid.append(list([int(x) for x in puzzle_line.strip()]))

@timer
def part1(grid: list[list[int]]):
    valid_trails = 0
    trailheads = find_trailheads(grid)

    for trailhead in trailheads:
        valid_trails += valid_trails_from_loc(grid, trailhead)

    print(f"Part 1: {valid_trails}")
    return True

@timer
def part2():
    print(f"Part 2: {TOTAL_TRAILS}")
    return True


def find_trailheads(grid: list[list[int]]) -> list[tuple[int, int]]:
    """
    Find all trailheads (value == 0) on the grid, return a list of coordinate
    tuples.
    """
    t_heads = []
    for y_idx, y in enumerate(grid):
        for x_idx, x in enumerate(y):
            if x == 0:
                t_heads.append((y_idx, x_idx))

    return t_heads


def bounds_check(grid: list[list[int]], y: int, x: int) -> bool:
    # set limits based on size of grid:
    max_depth = len(grid)-1
    max_width = len(grid[0])-1

    if (0 <= y <= max_depth and
        0 <= x <= max_width):
        return True
    return False


def valid_trails_from_loc(grid: list[list[int]], loc: tuple[int, int], elevation: int = 0, peaks_reached: set[tuple[int, int]] = set()) -> int:
    global TOTAL_TRAILS

    if elevation == 0:
        peaks_reached = set()

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

#        print(f"{loc} checking {direction} for {elevation + 1}")


        if not bounds_check(grid, new_y, new_x):
#            print(f"Out of Bounds: {(new_y, new_x)}")
            continue


        if grid[new_y][new_x] == elevation + 1:
            if grid[new_y][new_x] == 9:
#                print(f"Found peak: {(new_y, new_x)} going {direction}")
                TOTAL_TRAILS += 1
                peaks_reached.add((new_y, new_x))
                continue

#            print(f"coords: {(new_y, new_x)}, elevation: {elevation}, direction: {direction}")
            #XXX check if we've been here already and can re-use the value for number of valid trails
            valid_trails_from_loc(grid, (new_y, new_x), elevation + 1, peaks_reached)

#    print(f"done searching for {elevation}")
    return len(peaks_reached)



part1(grid)
part2()

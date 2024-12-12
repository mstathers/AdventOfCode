import time

def timer(func):
    def wrapper(*arg):
        start_t = time.perf_counter()
        res = func(*arg)
        end_t = time.perf_counter()
        elapsed_t = end_t - start_t
        print(f"Time taken: {elapsed_t:.6f} seconds")
        return res
    return wrapper

@timer
def part1(in_file: str) -> int:
    with open(in_file, 'r', encoding='utf8') as file:
        grid = []
        for garden_line in file.readlines():
            grid.append(list(garden_line.strip()))
#    print(grid)


    price = 0

    # Store tuple of coords for done squares
    done = set()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
#            print(f"{y},{x}")
            if (y, x) in done:
#                print(f"{y},{x} already done")
                continue

            area, perimeter = check_adjacent_squares(grid, (y, x), done, fresh=True)
            plot_price = area * perimeter
#            print(area, perimeter, plot_price)

            price += plot_price


    return price


def check_adjacent_squares(grid: list[list[str]], loc: tuple[int, int], done: set[tuple[int, int]], fresh: bool = False):
    y, x = loc
    cur_value = grid[y][x]
    area = 1
    perimeter = 4

    # When we start a fresh new Plot
    if fresh:
        perimeter = 4
#        print(f"Found {grid[y][x]} at {y},{x}. Perim: {perimeter}")
        done.add((y, x))


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


        if not bounds_check(grid, new_y, new_x):
#            print(f"Out of Bounds: {(new_y, new_x)}")
            continue

        new_value = grid[new_y][new_x]

        if (new_y, new_x) in done and cur_value == new_value:
#            print(f"{new_y},{new_x} already done (inside)")
            perimeter -= 1
            continue

        # matching
        if cur_value == new_value:
            perimeter -= 1
#            print(f"Found {grid[new_y][new_x]} at {new_y},{new_x}. Perim: {perimeter}")
            done.add((new_y, new_x))

            new_area, new_perimeter = check_adjacent_squares(grid, (new_y, new_x), done)
            area += new_area
            perimeter += new_perimeter

    return area, perimeter


def bounds_check(grid: list[list[str]], y: int, x: int) -> bool:
    # set limits based on size of grid:
    max_depth = len(grid)-1
    max_width = len(grid[0])-1

    if (0 <= y <= max_depth and
        0 <= x <= max_width):
        return True
    return False


print(f"Mini eg: {part1('mini-input.txt')}")
print(f"Test eg: {part1('test-input.txt')}")
print(f"Part 1: {part1('input.txt')}")

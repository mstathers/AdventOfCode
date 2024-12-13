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
def part1(in_file: str, p1=True) -> int:
    with open(in_file, 'r', encoding='utf8') as file:
        grid = []
        for garden_line in file.readlines():
            grid.append(list(garden_line.strip()))
#    print(grid)


    price = 0
    price_2 = 0

    # Store tuple of coords for done squares
    done = set()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
#            print(f"{y},{x}")
            if (y, x) in done:
#                print(f"{y},{x} already done")
                continue

            area, perimeter, corners = check_adjacent_squares(grid, (y, x), done, fresh=True)
            plot_price = area * perimeter

            sides_price = area * corners

#            print(grid[y][x], area, perimeter, corners, plot_price, sides_price)

            price += plot_price
            price_2 += sides_price


    if p1:
        return price
    else:
        return price_2


def check_adjacent_squares(grid: list[list[str]], loc: tuple[int, int], done: set[tuple[int, int]], fresh: bool = False):
    y, x = loc
    cur_value = grid[y][x]
    corners = 0
    adj_squares = {}
    area = 1
    perimeter = 4

    # When we start a fresh new Plot
    if fresh:
        perimeter = 4
#        print(f"Found {grid[y][x]} at {y},{x}. Perim: {perimeter}")
        done.add((y, x))


    for direction in ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']:
        if direction == 'n':
            new_y = y - 1
            new_x = x
        elif direction == 'ne':
            new_y = y - 1
            new_x = x + 1
        elif direction == 'e':
            new_y = y
            new_x = x + 1
        elif direction == 'se':
            new_y = y + 1
            new_x = x + 1
        elif direction == 's':
            new_y = y + 1
            new_x = x
        elif direction == 'sw':
            new_y = y + 1
            new_x = x - 1
        elif direction == 'w':
            new_y = y
            new_x = x - 1
        elif direction == 'nw':
            new_y = y - 1
            new_x = x - 1
        # We shouldn't ever get here
        else:
            new_y = -1
            new_x = -1


        if not bounds_check(grid, new_y, new_x):
#            print(f"Out of Bounds: {(new_y, new_x)}")
            continue

        new_value = grid[new_y][new_x]
        adj_squares[direction] = new_value

        if (direction == 'n' or
            direction == 'e' or
            direction == 's' or
            direction == 'w'):

            if (new_y, new_x) in done and cur_value == new_value:
    #            print(f"{new_y},{new_x} already done (inside)")
                perimeter -= 1
                continue

            # matching
            if cur_value == new_value:
                perimeter -= 1
    #            print(f"Found {grid[new_y][new_x]} at {new_y},{new_x}. Perim: {perimeter}")
                done.add((new_y, new_x))

                new_area, new_perimeter, new_corners = check_adjacent_squares(grid, (new_y, new_x), done)
                area += new_area
                perimeter += new_perimeter
                corners += new_corners

    # Work out if this is a corner by checking the values of adjacent squares.
    def is_corner(cur_value, adj_s, direction):
        if direction[0] in adj_s:
            side0 = adj_s[direction[0]]
        else:
            side0 = None
        if direction[1] in adj_s:
            diag = adj_s[direction[1]]
        else:
            diag = None
        if direction[2] in adj_s:
            side90 = adj_s[direction[2]]
        else:
            side90 = None


        if cur_value != side0 and cur_value != side90:
#            print(f"A: 0: {side0}, 90: {side90}")
            return True
        if cur_value != side0 and side90 is None:
#            print(f"B: 0: {side0}, 90: {side90}")
            return True
        if side0 is None and cur_value != side90:
#            print(f"C: 0: {side0}, 90: {side90}")
            return True
        if cur_value == side0 and cur_value != diag and cur_value == side90:
#            print(f"D: 0: {side0}, diag: {diag}, 90: {side90}")
            return True
        return False

    # CORNER CALCULATION
    for adj_set in [('n', 'ne', 'e'),
                    ('e', 'se', 's'),
                    ('s', 'sw', 'w'),
                    ('w', 'nw', 'n')]:
        if is_corner(cur_value, adj_squares, adj_set):
            corners += 1
#            print(f"{y}, {x} - {adj_set}: corners: {corners}")


#    print(f"{y}, {x}: corners: {corners}")


    return area, perimeter, corners


def bounds_check(grid: list[list[str]], y: int, x: int) -> bool:
    # set limits based on size of grid:
    max_depth = len(grid)-1
    max_width = len(grid[0])-1

    if (0 <= y <= max_depth and
        0 <= x <= max_width):
        return True
    return False


#print(f"P1 Mini eg: {part1('mini-input.txt')}")
#assert part1('mini-input.txt') == 140
#print(f"P1 Test eg: {part1('test-input.txt')}")
print(f"Part 1: {part1('input.txt')}")

#print(f"P2 Mini eg: {part1('mini-input.txt', False)}")
print(f"Part 2: {part1('input.txt', False)}")

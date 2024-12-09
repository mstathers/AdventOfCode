import itertools

with open('input.txt', 'r', encoding='utf8') as file:
    grid = []
    for puzzle_line in file.readlines():
        grid.append(list(puzzle_line.strip()))


def part1(grid: list[list[str]]):
    nodes = find_nodes(grid)
    total_on_grid_antinodes = find_antinodes(grid, nodes)

    print(f"Part 1: {total_on_grid_antinodes}")
    return True

def find_nodes(grid: list[list[str]]) -> dict[str, list[list[int]]]:
    '''
    Find frequencies and location of their nodes.
    eg.
    {'0': [[1, 8], [2, 5], [3, 7], [4, 4]], 'A': [[5, 6], [8, 8], [9, 9]]}
    '''
    nodes = {}

    # Populate nodes dict
    for y_idx, y in enumerate(grid):
        for x_idx, x in enumerate(y):
            if x == '.':
                continue

            if x not in nodes:
                nodes[x] = []

            nodes[x].append([y_idx, x_idx])
    return nodes

def find_antinodes(grid: list[list[str]], nodes: dict[str, list[list[int]]], harmonic: bool = False) -> int:
    # We'll use a set so they're unique
    total_antinodes = set()


    def bounds_check(grid: list[list[str]], y: int, x: int) -> bool:
        # set limits based on size of grid:
        max_depth = len(grid)-1
        max_width = len(grid[0])-1

        if (0 <= y <= max_depth and
            0 <= x <= max_width):
            return True
        return False


    def next_harmonic_node(grid: list[list[str]], y: int, x: int, y_difference: int, x_difference: int, direction: str = '-') -> bool:
        if direction == '-':
            new_y = y - y_difference
            new_x = x - x_difference
        elif direction == '+':
            new_y = y + y_difference
            new_x = x + x_difference
        # We shouldn't ever get here
        else:
            new_y = -1
            new_x = -1

        if bounds_check(grid, new_y, new_x):
            total_antinodes.add(f"{new_y},{new_x}")
            return next_harmonic_node(grid, new_y, new_x, y_difference, x_difference, direction)

        return False



    for freq_locs in nodes.values():
        loc_pairs = list(itertools.combinations(freq_locs, 2))

        for loc_pair in loc_pairs:
            y_difference = loc_pair[1][0] - loc_pair[0][0]
            x_difference = loc_pair[1][1] - loc_pair[0][1]

            # Part 1
            if not harmonic:
                # There is only ever two anti-nodes for two points
                # First potential anti-node
                new_y = loc_pair[0][0] - y_difference
                new_x = loc_pair[0][1] - x_difference

                if bounds_check(grid, new_y, new_x):
                    total_antinodes.add(f"{new_y},{new_x}")

                # Second potential anti-node
                new_y = loc_pair[1][0] + y_difference
                new_x = loc_pair[1][1] + x_difference

                if bounds_check(grid, new_y, new_x):
                    total_antinodes.add(f"{new_y},{new_x}")

            # Part 2
            # If we're looking for harmonic nodes, it's much like the above,
            # but we need to recurse in the direction of the resonance until
            # we're going to leave the grid.
            # Fortunately there are still only two directions we need to check.
            else:
                # If there are two antenna they will cause harmonic resonance
                # nodes upon each other, so we can just blindly add them to the
                # list of anti-nodes.
                total_antinodes.add(f"{loc_pair[0][0]},{loc_pair[0][1]}")
                total_antinodes.add(f"{loc_pair[1][0]},{loc_pair[1][1]}")

                # left/top node, going left/up
                next_harmonic_node(grid,
                                   loc_pair[0][0],
                                   loc_pair[0][1],
                                   y_difference,
                                   x_difference,
                                   '-')
                # right/bottom node, going right/down
                next_harmonic_node(grid,
                                   loc_pair[1][0],
                                   loc_pair[1][1],
                                   y_difference,
                                   x_difference,
                                   '+')

    return len(total_antinodes)

def part2(grid: list[list[str]]):
    nodes = find_nodes(grid)
    total_on_grid_antinodes = find_antinodes(grid, nodes, harmonic=True)

    print(f"Part 2: {total_on_grid_antinodes}")
    return True

part1(grid)
part2(grid)

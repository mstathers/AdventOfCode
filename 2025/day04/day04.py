"""
https://adventofcode.com/2025/day/4
"""
def part1(input_lines: str) -> None:
    movable_rolls = 0

    grid = {}
    for y, line in enumerate(input_lines.split('\n')):
        for x, val in enumerate(line):
            grid[(x, y)] = val

    rolls = [key for key, val in grid.items() if val == '@']

    for roll in rolls:
        if can_remove_roll(grid, roll):
            movable_rolls += 1

    print(f"Part 1: {movable_rolls}")


def part2(input_lines: str) -> None:
    removed_rolls = 0

    grid = {}
    for y, line in enumerate(input_lines.split('\n')):
        for x, val in enumerate(line):
            grid[(x, y)] = val

    removed_rolls = attempt_to_remove_rolls(grid, removed_rolls)
    print(f"Part 2: {removed_rolls}")


def attempt_to_remove_rolls(grid: dict, removed_rolls: int) -> int:
    removed_a_roll = False
    rolls = [key for key, val in grid.items() if val == '@']

    for roll in rolls:
        if can_remove_roll(grid, roll):
            removed_rolls += 1
            grid[roll] = '.'
            removed_a_roll = True

    if removed_a_roll:
        removed_rolls = attempt_to_remove_rolls(grid, removed_rolls)

    return removed_rolls


def can_remove_roll(grid: dict, pos: tuple) -> bool:
    adj_rolls = 0
    for adj_loc in get_neighbors(grid, pos):
        if grid[adj_loc] == '@':
            adj_rolls += 1

    if adj_rolls < 4:
        return True

    return False


def get_neighbors(grid: dict, pos: tuple) -> list[tuple]:
    x0, y0 = pos
    candidates = [
            (x0 - 1, y0),
            (x0 + 1, y0),
            (x0, y0 - 1),
            (x0, y0 + 1),
            (x0 - 1, y0 - 1),
            (x0 - 1, y0 + 1),
            (x0 + 1, y0 - 1),
            (x0 + 1, y0 + 1),
            ]
    return [p for p in candidates if p in grid]


if __name__ == '__main__':
    with open('input.txt', encoding="utf-8") as file:
        puzzle_input = file.read()
    part1(puzzle_input)
    part2(puzzle_input)

def part1(tachyon_manifold_diagram: str) -> None:
    splits = 0
    beam_cols = set()
    for line in [list(x) for x in tachyon_manifold_diagram.split('\n')]:
        for idx, col in enumerate(line):
            if col == "S":
                beam_cols.add(idx)

            if col == "^" and idx in beam_cols:
                beam_cols.add(idx - 1)
                beam_cols.add(idx + 1)
                splits += 1

                beam_cols.remove(idx)


    print(f"Part 1: {splits}")


def part2(tachyon_manifold_diagram: str) -> None:
    """
    Work up from the bottom, so that we can use a bottom-up solution.
    """
    paths = {}
    for y, line in enumerate(reversed(tachyon_manifold_diagram.split('\n'))):
        for x, col in enumerate(line):
            coord_sum = 0


            if col == "^":
                # We need to check left and right.
                for horiz_direction in [x+1, x-1]:
                    # The puzzle skips every other line, so we can look two down.
                    less_y = 2
                    while y - less_y > 0:
                        if (horiz_direction, y-less_y) in paths:
                            coord_sum += paths[(horiz_direction, y-less_y)]
                            break
                        less_y += 2

                    if y - less_y == 0:
                        coord_sum += 1

                paths[(x ,y)] = coord_sum


            """ If we find S, just return the very last value in the
            dictionary. Luckily there is always a single split below the start.
            Though if this wasn't the case, we could find a value immediately
            below the S, like we do with the other splits. """
            if col == "S":
                *_, last = paths.values()
                print(f"Part 2: {last}")

    #[print(f"{loc}: {val}") for loc, val in paths.items()]


if __name__ == '__main__':
    with open('input.txt', encoding="utf-8") as file:
        puzzle_input = file.read()
    part1(puzzle_input)
    part2(puzzle_input)

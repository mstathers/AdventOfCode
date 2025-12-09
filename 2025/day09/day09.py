def part1(red_tiles_input: str) -> None:
    tiles = []
    for line in red_tiles_input.splitlines():
        x, y = [(int(x)) for x in line.split(',')]
        tiles.append([x, y])

    #print(tiles)

    areas = {}
    for idx_1, tile_1 in enumerate(tiles):
        for idx_2, tile_2 in enumerate(tiles):
            if idx_1 == idx_2:
                continue

            if (idx_2, idx_1) in areas:
                continue

            x1 = tile_1[0]
            x2 = tile_2[0]
            y1 = tile_1[1]
            y2 = tile_2[1]

            area = (abs(x1-x2)+1) * (abs(y1-y2)+1)
            areas[(idx_1, idx_2)] = area

    sorted_areas = {k: v for k, v in sorted(areas.items(), key=lambda x: x[1], reverse=True)}

    #[print(k, v) for k, v in sorted_areas.items()]
    largest_area = next(iter(sorted_areas.values()))
    print(f"Part 1: {largest_area}")

def part2(red_tiles_input: str) -> None:
    grid = {}
    for line in red_tiles_input.splitlines():
        x, y = [(int(x)) for x in line.split(',')]
        grid[(x, y)] = '#'

    

    print(grid)

if __name__ == '__main__':
    with open('test-input.txt', encoding="utf-8") as file:
        puzzle_input = file.read()
    part1(puzzle_input)
    part2(puzzle_input)

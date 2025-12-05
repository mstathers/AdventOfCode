def part1(ingredient_db: str) -> None:
    fresh_ingredient_ranges = {}
    spoiled_ingredient_ids = []
    fresh_ingredient_ids = []

    # Put together dict of fresh ingredients first
    for line in ingredient_db.split('\n'):
        # skip blank lines
        if not line:
            continue

        # fresh ingredient range
        if "-" in line:
            start, end = [int(x) for x in line.split('-')]

            if start in fresh_ingredient_ranges:
                current_end = fresh_ingredient_ranges[start]
                if current_end > end:
                    continue

            fresh_ingredient_ranges[start] = end
            continue


        # Actually check ingredients
        fresh = False
        ingredient = int(line)
        for start, end in fresh_ingredient_ranges.items():
            if start <= ingredient <= end:
                #print(f"Fresh: {start} <= {ingredient} <= {end}")
                fresh_ingredient_ids.append(ingredient)
                fresh=True
                break

        if not fresh:
#            print(f"Spoiled: {ingredient}")
            spoiled_ingredient_ids.append(ingredient)


#    print(len(fresh_ingredient_ids))
#    print(len(spoiled_ingredient_ids))
#    print(len(fresh_ingredient_ids) + len(spoiled_ingredient_ids))
#    print(len(fresh_ingredient_ranges))
#    print(fresh_ingredient_ranges)
    print(f"Part 1: {len(fresh_ingredient_ids)}")

def part2(ingredient_db: str) -> None:
    fresh_ingredient_ranges = {}
    for line in ingredient_db.split('\n'):
        if "-" in line:
            start, end = [int(x) for x in line.split('-')]

            if start in fresh_ingredient_ranges:
                current_end = fresh_ingredient_ranges[start]
                if current_end > end:
                    continue

            fresh_ingredient_ranges[start] = end

    updated = True
    while updated:
        fresh_ingredient_ranges, updated = merge_ranges(fresh_ingredient_ranges)

    total_fresh_ingredients = 0
    for start, end in fresh_ingredient_ranges.items():
        total_fresh_ingredients += end - start + 1


#    print(fresh_ingredient_ranges)
    print(f"Part 2: {total_fresh_ingredients}")

def merge_ranges(ranges: dict, updated: bool = False) -> tuple[dict, bool]:
    for start, end in ranges.copy().items():
        for current_start, current_end in ranges.copy().items():
            #print(f"checking {start}-{end} against {current_start}-{current_end}")
            if current_start < start <= current_end:
                #print(f"{start} between {current_start}-{current_end}")
                ranges[current_start] = max(current_end, end)
                updated = True

            elif start < current_start <= end:
                ranges.pop(current_start)
                ranges[start] = max(current_end, end)
                updated = True

    return (ranges, updated)



if __name__ == '__main__':
    with open('input.txt', encoding="utf-8") as file:
        puzzle_input = file.read()
    part1(puzzle_input)
    part2(puzzle_input)

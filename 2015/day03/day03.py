with open('input') as file:
    directions = file.read()

def part1(directions):
    houses = {}
    coords = [0, 0]
    for direction in directions:
        cur_coord = f"{coords[0]},{coords[1]}"
        if cur_coord in houses:
            houses[cur_coord] += 1
        else:
            houses[cur_coord] = 1

        match direction:
            case '>':
                coords[0] += 1
            case '<':
                coords[0] -= 1
            case '^':
                coords[1] += 1
            case 'v':
                coords[1] -= 1

    duplicate_gifts = 0
    for value in houses.values():
        if value > 0:
            duplicate_gifts += 1

    print(f"Part 1: {duplicate_gifts}")
    return True

def part2(directions):
    # Flag to alternate between santa and robo-santa
    is_santa = True

    houses = {}
    santa_coords = [0, 0]
    robo_coords = [0, 0]

    def coord_adjust(coords: list, direction: str) -> list:
        match direction:
            case '>':
                coords[0] += 1
            case '<':
                coords[0] -= 1
            case '^':
                coords[1] += 1
            case 'v':
                coords[1] -= 1

        return coords


    for direction in directions:
        if is_santa:
            cur_coord = f"{santa_coords[0]},{santa_coords[1]}"
            santa_coords = coord_adjust(santa_coords, direction)
            is_santa = False # Robo's turn
        else:
            cur_coord = f"{robo_coords[0]},{robo_coords[1]}"
            robo_coords = coord_adjust(robo_coords, direction)
            is_santa = True # Santa's turn

        if cur_coord in houses:
            houses[cur_coord] += 1
        else:
            houses[cur_coord] = 1

    duplicate_gifts = 0
    for value in houses.values():
        if value > 0:
            duplicate_gifts += 1

    print(f"Part 2: {duplicate_gifts}")
    return True

part1(directions)
part2(directions)

with open('input') as file:
    input_list = file.readlines()

def part1(input_list):
    totalSurfaceArea = 0
    for gift in input_list:
        # [3, 11, 24]
        dim = [int(x) for x in gift.strip().split('x')]
        # Sorted so the shortest sides are always first
        dim.sort()

        # Need to get the surface aread of the box, plus the area of the
        # smallest side for "extra".
        surfaceAreaPlusExtra = 2*dim[0]*dim[1]+2*dim[1]*dim[2]+2*dim[2]*dim[0]+dim[0]*dim[1]

        totalSurfaceArea += surfaceAreaPlusExtra


    print(f"Part 1: {totalSurfaceArea}")
    return True

def part2(input_list):
    totalRibbon = 0
    for gift in input_list:
        # [3, 11, 24]
        dim = [int(x) for x in gift.strip().split('x')]
        # Sorted so the shortest sides are always first
        dim.sort()

        perimeter = 2*dim[0]+2*dim[1]
        bow = dim[0]*dim[1]*dim[2]

        totalRibbon += perimeter + bow


    print(f"Part 2: {totalRibbon}")
    return True

part1(input_list)
part2(input_list)

from typing import Counter


with open('test-input.txt', 'r', encoding='utf8') as file:
    rawdisk = [int(x) for x in list(file.read().strip())]

def part1(rawdisk: list[int]):
    exploded_disk = explode_disk(rawdisk)

    defragged_disk = defrag_disk(exploded_disk)

    checksum = calc_checksum(defragged_disk)

    print(f"Part 1: {checksum}")
    return True

def explode_disk(disk: list[int]):
    new_disk = []
    for idx_i, i in enumerate(disk):
        file_id = int(idx_i/2)

        # file block
        if idx_i % 2 == 0:
            if i == 0:
                print("Length of file block cannot be zero")
                raise
            for _ in range(i):
                new_disk.append(file_id)

        # blank spaces
        else:
            for _ in range(i):
                new_disk.append('.')

    return new_disk

# Cool recursive function that failed due to max recursion depth with real
# input .:(
def move_last_element_into_empty_spot(disk: list):
    # remove spaces
    if disk[-1] == '.':
        disk.pop()
        return move_last_element_into_empty_spot(disk)

    try:
        empty_slot = disk.index('.')
        disk[empty_slot] = disk.pop()
        return move_last_element_into_empty_spot(disk)
    except ValueError:
        return disk

def defrag_disk(disk: list):
    while True:
        if disk[-1] == '.':
            disk.pop()
            continue
        try:
            empty_slot = disk.index('.')
            disk[empty_slot] = disk.pop()
            continue
        except ValueError:
            return disk

def calc_checksum(disk: list[int]) -> int:
    total = 0
    for idx_i, i in enumerate(disk):
        if i == '.':
            continue
        total += idx_i * i
    return total


def part2(rawdisk: list[int]):
    exploded_disk = explode_disk(rawdisk)

    print(exploded_disk)
    defragged_disk = whole_disk_defrag(exploded_disk)

    checksum = calc_checksum(defragged_disk)
    print(f"Part 2: {checksum}")
    return True


def whole_disk_defrag(disk: list):
    file_sizes = Counter(disk)
    rear_value = disk[-1]
    while True:
        if rear_value == 0:
            break
        rear_size = file_sizes[rear_value]
        print(f"file_id: {rear_value}, file_size: {rear_size}")

        last_empty_index = 0
        found = False
        while not found:
            try:
                empty_block = disk.index('.', last_empty_index + 1)
            except ValueError:
                break
            print(f"checking {empty_block}")
            for i in range(rear_size):
                #print(i)
                if disk[empty_block + i] != '.':
                    last_empty_index = empty_block
                    print(f"next block is not empty. Setting last_empty_index to {last_empty_index}")
                    break


                if i == rear_size-1:
                    print(f"file_id {rear_value} will fit starting at index: {empty_block}")

                    # Remove current file
                    del disk[disk.index(rear_value): disk.index(rear_value)+rear_size] # XXX
                    # Add file to empty spot
                    for j in range(rear_size):
                        disk[empty_block + j] = rear_value
                        #disk.pop() #XXX
                        #disk.reverse().remove(rear_value)

                    found = True


        print(disk)
        rear_value -= 1

    return disk




part1(rawdisk)
part2(rawdisk)

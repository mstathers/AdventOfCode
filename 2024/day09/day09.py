from typing import Counter


with open('input.txt', 'r', encoding='utf8') as file:
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
                raise AssertionError("Length of file block cannot be zero")
            for _ in range(i):
                new_disk.append(file_id)

        # blank spaces
        else:
            for _ in range(i):
                new_disk.append('.')

    return new_disk

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

#    print(exploded_disk)
    defragged_disk = whole_disk_defrag(exploded_disk)

    checksum = calc_checksum(defragged_disk)
    print(f"Part 2: {checksum}")
    return True


def whole_disk_defrag(disk: list):
    # Gives us all files and a length of each file.
    file_sizes = Counter(disk)
    # We start at the back.
    file_id = disk[-1]

    while True:
        # Don't bother checking further if we get to file id 0
        if file_id == 0:
            break

        # Save file size from counter for later
        file_size = file_sizes[file_id]

        cur_file_location = disk.index(file_id)
        last_empty_index = 0

        found = False
        while not found:
            # Get start of next block of empty space.
            try:
                empty_block = disk.index('.', last_empty_index + 1)
            except ValueError:
                break

            # Don't bother checking to the right of the current location
            if empty_block > cur_file_location:
                break

            # Check block of empty space to see if it can fit our file.
            for i in range(file_size):
                if disk[empty_block + i] != '.':
                    last_empty_index = empty_block
                    break


                # It can fit our file!
                if i == file_size-1:
                    # Remove current file from its current location, replacing with empty space.
                    for _ in range(file_size):
                        disk[disk.index(file_id)] = '.'

                    # Add file to empty spot
                    for j in range(file_size):
                        disk[empty_block + j] = file_id

                    found = True

        # check the next file
        file_id -= 1

    return disk




part1(rawdisk)
part2(rawdisk)

"""
https://adventofcode.com/2025/day/2
"""

def part1(product_ranges: str) -> int:
    """
    day2p1
    """
    invalid_id_sum = 0

    product_id_ranges = product_ranges.split(',')
    for product_id_range in product_id_ranges:
        current_id, end_id = [int(x) for x in product_id_range.split('-')]

        while current_id <= end_id:
            #check if number has even number of digits
            current_id_list = list(str(current_id))
            if len(current_id_list) % 2:
                current_id += 1
                continue

            half_list_length = int(len(current_id_list)/2)


            first_half = current_id_list[:half_list_length]
            last_half = current_id_list[half_list_length:]

            if first_half == last_half:
                invalid_id_sum += current_id

            current_id += 1
    return invalid_id_sum

def part2(product_ranges: str) -> int:
    """
    day2p2
    """
    invalid_id_sum = 0

    product_id_ranges = product_ranges.split(',')
    for product_id_range in product_id_ranges:
        current_id, end_id = [int(x) for x in product_id_range.split('-')]
        for current_id in range(current_id, end_id+1):
            current_id_list = list(str(current_id))
            for parts in range(2, len(current_id_list)+1):
                if len(current_id_list) % parts == 0:
                    #                    print(f"{current_id} (len of {len(current_id_list)}) splits into {parts} parts")
                    section_length = int(len(current_id_list) / parts)
                    sections = set()
                    for i in range(0, len(current_id_list), section_length):
                        section = current_id_list[i:i+section_length]
                        sections.add(''.join(map(str,section)))

                    if len(sections) == 1:
                        invalid_id_sum += current_id
#                        print(f"invalid id: {current_id}")
                        break

            current_id += 1



    return invalid_id_sum

if __name__ == '__main__':
    with open('input.txt', encoding="utf-8") as file:
        puzzle_lines = file.read().strip()
    print(part1(puzzle_lines))
    print(part2(puzzle_lines))

"""
https://adventofcode.com/2025/day/3
"""
def part1(battery_banks: list) -> int:
    total_joltage = 0

    for battery_bank in battery_banks:
        #print(battery_bank)

        batteries = list(battery_bank)
        batteries = [int(s) for s in list(battery_bank)]
        bank_length = len(batteries)

        biggest_battery = 0
        after_biggest_battery = 0

        for idx, battery in enumerate(batteries):
            #print(f"{idx}/{bank_length-1}: {battery}")

            if battery > biggest_battery and idx != bank_length-1:
                biggest_battery = battery
                after_biggest_battery = 0
                continue

            if battery > after_biggest_battery:
                after_biggest_battery = battery
                continue

        #print(biggest_battery, after_biggest_battery)

        total_joltage += int(str(biggest_battery) + str(after_biggest_battery))

    return total_joltage

def part2(battery_banks: list) -> int:
    """
    This method improves a lot on the last. We can actually use this for part 1
    if we change the ALLOWED_BANK_LENGTH to 2.

    We will calculate how many "skips" we're allowed. Everytime we iterate
    through the batteries, we can check ahead by how many skips we have left.
    If we find a greater number within our skip range, we can skip our current
    battery and subtract one skip from our remaining skips allowed..
    """
    ALLOWED_BANK_LENGTH = 12
    total_joltage = 0

    for battery_bank in battery_banks:
        #print(battery_bank)
        batteries = [int(s) for s in list(battery_bank)]
        bank_length = len(batteries)

        allowed_skips = bank_length - ALLOWED_BANK_LENGTH

        joltage = ''
        for idx, battery in enumerate(batteries):
            skip=False
            for i in range(1, allowed_skips+1):
                if idx+i >= bank_length: # avoid out of bounds
                    break

                next_bat = batteries[idx+i]

                if next_bat > battery:
                    skip=True
                    break

            if skip:
                allowed_skips -= 1
                continue

            joltage += str(battery)

            if len(joltage) == ALLOWED_BANK_LENGTH:
                break

        total_joltage += int(joltage)


    return total_joltage

if __name__ == '__main__':
    with open('test-input.txt') as file:
        puzzle_lines = file.read().splitlines()
    print(part1(puzzle_lines))
    print(part2(puzzle_lines))

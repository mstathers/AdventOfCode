from functools import cache
import time

def timer(func):
    def wrapper(*arg):
        start_t = time.perf_counter()
        res = func(*arg)
        end_t = time.perf_counter()
        elapsed_t = end_t - start_t
        print(f"Time taken: {elapsed_t:.6f} seconds")
        return res
    return wrapper

@cache
def evaluate_stone_depth(pebble: int, max_depth, cur_depth=0):
    if cur_depth == max_depth:
#        print(f"returning {pebble}")
        return 1
#    print(f"pebble: {pebble}, cur_depth: {cur_depth}")

    cur_depth+=1


    # 0 to 1
    if pebble == 0:
        return evaluate_stone_depth(1, max_depth, cur_depth)

    pebble_len = len(str(pebble))
    if pebble_len % 2 == 0:

        l_pebble = list(str(pebble))
        r_pebble = []

        for _ in range(pebble_len // 2):
            r_pebble.append(l_pebble.pop())
        r_pebble.reverse()


        #new_stones.append(int(''.join(l_pebble)))
        l_pebble = int(''.join(l_pebble))
#        print(f"l_pebble: {l_pebble}, cur_depth: {cur_depth}")
        l_path = evaluate_stone_depth(l_pebble, max_depth, cur_depth)
        #new_stones.append(int(''.join(r_pebble)))
        #stone_count += 1
        r_pebble = int(''.join(r_pebble))
#        print(f"r_pebble: {r_pebble}, cur_depth: {cur_depth}")
        r_path = evaluate_stone_depth(r_pebble, max_depth, cur_depth)

        return l_path + r_path

    # Else, value * 2024
    pebble = pebble * 2024
    return evaluate_stone_depth(pebble, max_depth, cur_depth)





@timer
def blink_at_stones(in_file: str, blinks: int = 25):
    with open(in_file, 'r', encoding='utf8') as fh:
        stones = [int(x) for x in fh.read().strip().split()]
#    print(stones)

    stone_count = 0
    for stone in stones:
        stone_count += evaluate_stone_depth(stone, blinks)
#        print(f"Current stone count after evaluating stone {stone}: {stone_count}")

    return stone_count


### THE BELOW NEVER GETS RAN. MY ORIGINAL PART 1

    for _ in range(blinks):
        new_stones = []

        while stones:
            pebble = stones.pop()

            if pebble == 0:
                new_stones.append(1)
                continue

            pebble_len = len(str(pebble))
            if pebble_len % 2 == 0:
                l_pebble = list(str(pebble))
                r_pebble = []

                for _ in range(pebble_len // 2):
                    r_pebble.append(l_pebble.pop())
                r_pebble.reverse()

                new_stones.append(int(''.join(l_pebble)))
                new_stones.append(int(''.join(r_pebble)))
                continue

            # Else
            new_stones.append(pebble * 2024)

        stones = new_stones
#        print(stones)

    return len(stones)

test_stones = blink_at_stones('test-input.txt')
print(f"Example input: {test_stones}\n")
assert test_stones == 55312

print(f"Part 1: {blink_at_stones('input.txt')}")
print(f"Part 2: {blink_at_stones('input.txt', 75)}")

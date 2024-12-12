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


@timer
def blink_at_stones(in_file: str, blinks: int = 25):
    with open(in_file, 'r', encoding='utf8') as fh:
        stones = [int(x) for x in fh.read().strip().split()]
#    print(stones)

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
print(f"Test input: {test_stones}\n")
assert test_stones == 55312

print(f"Part 1: {blink_at_stones('input.txt')}")
#print(f"Part 2: {blink_at_stones('input.txt', 75)}")

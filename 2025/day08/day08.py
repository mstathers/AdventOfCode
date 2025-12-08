import numpy as np

def parts_1_and_2(junction_list: str) -> None:
    junctions = []
    for line in junction_list.split('\n'):
        if not line:
            continue
        x, y, z = [(int(x)) for x in line.split(',')]
        junctions.append([x, y, z])

    #print(junctions)

    distances = find_all_distances_between_junctions(junctions)

    circuits = []

    # For the test input, we look after 10 connections. For the real input, we
    # need to look after 1000 connections.
    if len(junctions) == 20:
        max_iterations = 10
    else:
        max_iterations = 1000
    iter_counter = 0

    d_iter = iter(distances)
    while True:
        iter_counter += 1
#        print(f"unconnected_junctions: {len(unconnected_junctions)}")

        next_shortest = next(d_iter)
#        print(f"next_shortest connection: {next_shortest}")
        p1, p2 = next_shortest

        p1_circuit = None
        p2_circuit = None

        for cir_idx, circuit in enumerate(circuits):
            if junctions[p1] in circuit:
#                print(f"found {p1}: {junctions[p1]} already in {circuit}")
                p1_circuit = cir_idx
            if junctions[p2] in circuit:
#                print(f"found {p2}: {junctions[p2]} already in {circuit}")
                p2_circuit = cir_idx

        if p1_circuit is None and p2_circuit is None:
            circuits.append([junctions[p1], junctions[p2]])
        if p1_circuit == p2_circuit:
            pass
        elif p1_circuit is not None and p2_circuit is not None:
#            print("both junctions in existing connections")
            circuits[p1_circuit] = circuits[p1_circuit] + circuits[p2_circuit]
#            print(f"New circuit at idx {p1_circuit}: {circuits[p1_circuit]}")

#            print(f"removing idx {p2_circuit}: {circuits[p2_circuit]}")
            circuits.pop(p2_circuit)
        elif p1_circuit is not None:
#            print(f"Adding {junctions[p2]} to {circuits[p1_circuit]}")
            circuits[p1_circuit].append(junctions[p2])
            #print(circuits[p1_circuit])
        elif p2_circuit is not None:
            circuits[p2_circuit].append(junctions[p1])
            #print(circuits[p2_circuit])
        #else:
        #    print('idk, lol')

#        print('========= full circuits =========')
#        for cir in circuits:
#            print(f"{len(cir)}: {cir}")
#
#        print('-------------------------------------------')

        # P1. we'll output our answer when our iterations hit the p1 limit.
        if iter_counter == max_iterations:
            p1_total = np.prod(np.array(sorted([len(x) for x in circuits], reverse=True)[:3]))
            print(f"Part 1: {p1_total}")

        # P2. If there is only one circuit left, and it has all the junctions in it.
        if len(circuits) == 1 and len(circuits[0]) == len(junctions):
            last_junctions = []
            last_junctions.append(junctions[p1])
            last_junctions.append(junctions[p2])

            #print(last_junctions)
            total = np.prod(np.array([x[0] for x in last_junctions]))
            print(f"Part 2: {total}")

            return



def find_all_distances_between_junctions(junctions:list[list]) -> dict[tuple[int], float]:
    """
    https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html
    """
    distances = {}

    for idx_1, junct_1 in enumerate(junctions):
        for idx_2, junct_2 in enumerate(junctions):
            if idx_1 == idx_2:
                continue

            if (idx_2, idx_1) in distances:
                continue

            p1 = np.array(junct_1)
            p2 = np.array(junct_2)

            distance = np.linalg.norm(p1 - p2)

            distances[(idx_1, idx_2)] = distance

    sorted_distances = {k: v for k, v in sorted(distances.items(), key=lambda x: x[1])}

    return sorted_distances


if __name__ == '__main__':
    with open('input.txt', encoding="utf-8") as file:
        puzzle_input = file.read()
    parts_1_and_2(puzzle_input)

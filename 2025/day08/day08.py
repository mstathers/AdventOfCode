import numpy as np

def part1(junction_list: str) -> None:
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
        iterations = 10
    else:
        iterations = 1000

    d_iter = iter(distances)
    for _ in range(iterations):
        next_shortest = next(d_iter)
        print(f"next_shortest connection: {next_shortest}")
        p1, p2 = next_shortest

        p1_circuit = None
        p2_circuit = None

        for cir_idx, circuit in enumerate(circuits):
            if junctions[p1] in circuit:
                print(f"found {p1}: {junctions[p1]} already in {circuit}")
                p1_circuit = cir_idx
            if junctions[p2] in circuit:
                print(f"found {p2}: {junctions[p2]} already in {circuit}")
                p2_circuit = cir_idx

        if p1_circuit is None and p2_circuit is None:
            circuits.append([junctions[p1], junctions[p2]])
        if p1_circuit == p2_circuit:
            continue
        elif p1_circuit is not None and p2_circuit is not None:
            print("both junctions in existing connections")
            circuits[p1_circuit] = circuits[p1_circuit] + circuits[p2_circuit]
            print(f"New circuit at idx {p1_circuit}: {circuits[p1_circuit]}")

            print(f"removing idx {p2_circuit}: {circuits[p2_circuit]}")
            circuits.pop(p2_circuit)
        elif p1_circuit is not None:
            print(f"Adding {junctions[p2]} to {circuits[p1_circuit]}")
            circuits[p1_circuit].append(junctions[p2])
            #print(circuits[p1_circuit])
        elif p2_circuit is not None:
            circuits[p2_circuit].append(junctions[p1])
            #print(circuits[p2_circuit])
        else:
            print('idk, lol')

        print('========= full circuits =========')
        for cir in circuits:
            print(f"{len(cir)}: {cir}")

        print('-------------------------------------------')


    #print(circuits)
    #print('========= full circuits =========')
    #for cir in circuits:
    #    print(f"{len(cir)}: {cir}")


    total = np.prod(np.array(sorted([len(x) for x in circuits], reverse=True)[:3]))

    print(f"Part 1: {total}")




def find_all_distances_between_junctions(junctions:list[list]) -> dict[tuple[int], float]:
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
    part1(puzzle_input)

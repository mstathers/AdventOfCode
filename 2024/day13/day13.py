with open('test-input.txt', 'r', encoding='utf8') as fh:
    machines = [x.strip().split('\n') for x in fh.read().split('\n\n')]


for machine in machines:
    print(machine)


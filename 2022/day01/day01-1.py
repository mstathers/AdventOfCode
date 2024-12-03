elves=[]
elves.append(0)

with open("day01.input", "r") as f:
    for line in f:

        if line == "\n":
            elves.append(0)
            continue

        calories = int(line.strip())
        elves[-1] = elves[-1] + calories



#print(elves)


elves.sort(reverse=True)


topThree = 0
for i in range(3):
    topThree += elves[i]

print(topThree)


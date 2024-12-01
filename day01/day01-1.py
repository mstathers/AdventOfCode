#!/usr/bin/env python3

with open('input') as file:
    input_list = file.readlines()

list_one = []
list_two = []
for line in input_list:
    line_array = line.strip().split()

    list_one.append(int(line_array[0]))
    list_two.append(int(line_array[1]))

list_one.sort()
list_two.sort()

total=0
# we'll assume both lists are the same length
for i in range(len(list_one)):
    total+=abs(list_one[i] - list_two[i])

print(total)

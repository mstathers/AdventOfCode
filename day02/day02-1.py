#!/usr/bin/env python3

with open('input.txt') as file:
    input_list = file.readlines()

counter = 0
for report in input_list:
    levels = [int(x) for x in report.split()]

    increasing = 0
    decreasing = 0
    bad = 0

    for i in range(len(levels)):
        # don't check the last item
        if i == len(levels)-1:
            break

        # check if increasing
        if levels[i] > levels[i+1]:
            increasing = 1
        # or decreasing
        elif levels[i] < levels[i+1]:
            decreasing = 1
        # if the same level, discard
        elif levels[i] == levels[i+1]:
            bad = 1
            break

        # if we've been increasing AND decreasing, bad
        if increasing == 1 and decreasing == 1:
            bad = 1
            break

        # the difference between two adjacent levels can only be 3 or less.
        if abs(levels[i] - levels[i+1]) > 3:
            bad = 1
            break

    if bad == 0:
        counter += 1

print(counter)

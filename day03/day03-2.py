#!/usr/bin/env python3
import re

with open('input.txt') as file:
    input_str = file.read()

regPattern=r'(do\(\)|don\'t\(\)|mul\(([0-9]{1,3}),([0-9]{1,3})\))'
matches = re.findall(regPattern, input_str)

do = 1 #flag to do or don't include following mul() ops.
total = 0
for match in matches:
    if 'do()' in match[0]:
        do = 1
    elif 'don\'t()' in match[0]:
        do = 0

    if do == 0:
        continue

    if 'mul(' in match[0]:
        total += int(match[1]) * int(match[2])

print(total)

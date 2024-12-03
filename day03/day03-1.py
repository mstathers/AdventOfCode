#!/usr/bin/env python3
import re

with open('input.txt') as file:
    input_str = file.read()


regPattern=r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'
matches = re.findall(regPattern, input_str)


total = 0
for match in matches:
    total += int(match[0]) * int(match[1])

print(total)

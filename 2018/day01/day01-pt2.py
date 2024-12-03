#!/usr/bin/env python3

import re

freq=0
freqList = []

while True:
    with open("input.txt") as file:
        lines = file.read().splitlines()
        for line in lines:
            if freq in freqList:
                print("duplicate: {}".format(freq))
                break
            else:
                freqList.append(freq)

            offset = int(re.findall("([0-9]+)", line)[0])
#            print(line)
            if "+" in line:
                freq += offset
            elif "-" in line:
                freq -= offset
            else:
                print("MISSING + OR -")

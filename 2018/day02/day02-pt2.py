#!/usr/bin/env python3

import string

hashes={}
with open("input.txt") as file:
    lines = file.read().splitlines()

    for line in lines:
        if line not in hashes:
            hashes[line] = []

        allLetters = list(line)
        for letter in allLetters:
            alphaIndex = string.ascii_lowercase.index(letter)
            hashes[line].append(alphaIndex)

for outerCrate, outerHash in hashes.items():
    for innerCrate, innerHash in hashes.items():

        if outerCrate == innerCrate:
            continue

        garbage = 0
        diffCount = 0
        diffIndex = 0

        for index, outerNum in enumerate(outerHash):
            innerNum = innerHash[index]

#            print("comparing: {} {}".format(outerNum, innerNum))
            # the same
            if outerNum == innerNum:
                continue
            elif abs(outerNum - innerNum) >= 1:
                diffCount += 1
#                print("index: {}".format(index))
                diffIndex = index
                continue

        if diffCount == 1:
            del outerHash[diffIndex]
            for value in outerHash:
                print(string.ascii_lowercase[value], end='')
            print()
            exit()

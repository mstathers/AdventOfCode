#!/usr/bin/env python3

two=0
three=0
with open("input.txt") as file:
    lines = file.read().splitlines()
    for line in lines:
        allLetters = list(line)
        letterCount={}
        for letter in allLetters:
            if letter in letterCount:
                letterCount[letter] += 1
            else:
                letterCount[letter] = 1


        if 2 in letterCount.values():
            two += 1
        if 3 in letterCount.values():
            three += 1


print(two * three)

# Advent of Code 2022 - Puzzle 6-2

puzzleinput = ''

with open('input.txt', 'r') as file:
    for line in file:
        puzzleinput = line

for c in range(13,len(puzzleinput) - 1):
    block_of_14 = []
    for x in range(c, c - 14, -1):
        block_of_14.append(puzzleinput[x])

    if len(block_of_14) == len(set(block_of_14)):
        print(block_of_14)
        print('Marker found: ', c + 1)
        break
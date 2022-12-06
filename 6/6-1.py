# Advent of Code 2022 - Puzzle 6-1

puzzleinput = ''

with open('input.txt', 'r') as file:
    for line in file:
        puzzleinput = line

for c in range(3,len(puzzleinput) - 1):
    block_of_4 = []
    block_of_4.append(puzzleinput[c])
    block_of_4.append(puzzleinput[c-1])
    block_of_4.append(puzzleinput[c-2])
    block_of_4.append(puzzleinput[c-3])
    if len(block_of_4) == len(set(block_of_4)):
        print('Marker found: ', c + 1)
        break
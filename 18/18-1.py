# Advent of Code 2022 - Puzzle 18-1

import numpy

puzzleinput = []

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip('\n')
        puzzleinput.append(line)

# Get max dimensions of space
max_x = 0
max_y = 0
max_z = 0

for line in puzzleinput:
    line = line.split(',')
    if int(line[0]) > max_x:
        max_x = int(line[0])
    if int(line[1]) > max_y:
        max_y = int(line[1])
    if int(line[2]) > max_z:
        max_z = int(line[2])

# Some blocks have 0 as a position, so increment all positions by 1 to build an extra layer of blocks to hack around this
# Create array three blocks larger
lava = numpy.zeros((max_x+3) * (max_y+3) * (max_z+3),numpy.int8)
lava = lava.reshape(max_x+3, max_y+3, max_z+3)
lava[:] = 0

for line in puzzleinput:
    line = line.split(',')
    lava[int(line[0])+1][int(line[1])+1][int(line[2])+1] = 1

sides_visible = 0

# For each block, check if sides are visible
for x in range(0, max_x+3):
    for y in range(0, max_y+3):
        for z in range(0, max_z+3):
            if lava[x][y][z] == 1:
                if lava[x-1][y][z] == 0:
                    sides_visible += 1
                if lava[x+1][y][z] == 0:
                    sides_visible += 1
                if lava[x][y-1][z] == 0:
                    sides_visible += 1
                if lava[x][y+1][z] == 0:
                    sides_visible += 1
                if lava[x][y][z-1] == 0:
                    sides_visible += 1
                if lava[x][y][z+1] == 0:
                    sides_visible += 1

print("Sides visible:",sides_visible)

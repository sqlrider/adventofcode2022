# Advent of Code 2022 - Puzzle 18-2

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

# Part 2

# Need to get exterior faces only, so add water/steam (value 2) - if in an empty block, fill it with water if any touching block is also water.
# Do this instead of counting internal spaces and subtracting sides, as those spaces won't neccessarily be single blocks, and counting those 
# internal spaces correctly would involve recursion

# Seed edges of grid with water first
# x/y sides
for x in range(0, max_x+3):
    for y in range(0, max_y+3):
        lava[x][y][0] = 2
        lava[x][y][max_z+2] = 2
# y/z sides
for y in range(0, max_y+3):
    for z in range(0, max_z+3):
        lava[0][y][z] = 2
        lava[max_x+2][y][z] = 2
# x/z sides
for x in range(0, max_x+3):
    for z in range(0, max_z+3):
        lava[x][0][z] = 2
        lava[x][max_y+2][z] = 2


# This is nasty brute-force stuff, but quicker to code than 'flooding' the water from each of the 6 sides, and still runs in sub 1s
# Add water for any block currently touching water, this misses some air spaces on first run due to sequential nature,
# but can be re-ran until number of exposed surfaces doesn't change, because at least 1 block will change on every run until all 
# space is filled.

last_sides_visible = 0
water_everywhere = False

while(water_everywhere == False):

    for x in range(1, max_x+2):
        for y in range(1, max_y+2):
            for z in range(1, max_z+2):
                if lava[x][y][z] == 0:
                    if lava[x-1][y][z] == 2 or lava[x+1][y][z] == 2 or lava[x][y-1][z] == 2 or lava[x][y+1][z] == 2 or lava[x][y][z-1] == 2 or lava[x][y][z+1] == 2:
                        lava[x][y][z] = 2

    sides_visible = 0

    # Now water has filled what it can on this run, we re-iterate over the structure and count the sides that face water
    for x in range(1, max_x+2):
        for y in range(1, max_y+2):
            for z in range(1, max_z+2):
                if lava[x][y][z] == 1:
                    if lava[x-1][y][z] == 2:
                        sides_visible += 1
                    if lava[x+1][y][z] == 2:
                        sides_visible += 1
                    if lava[x][y-1][z] == 2:
                        sides_visible += 1
                    if lava[x][y+1][z] == 2:
                        sides_visible += 1
                    if lava[x][y][z-1] == 2:
                        sides_visible += 1
                    if lava[x][y][z+1] == 2:
                        sides_visible += 1

    if sides_visible != last_sides_visible:
        print("Water still spreading -",sides_visible," sides visible")
        last_sides_visible = sides_visible
    else:
        water_everywhere = True

print("Water filled, sides visible: ",sides_visible)

debug = False
if debug == True:
    for x in range(0,max_x+3):
        for y in range(0,max_y+3):
            for z in range(0,max_z+3):
                print(lava[x][y][z],end='')
            print()
        print()



# Advent of Code 2022 - Puzzle 23-1

import numpy

puzzleinput = []

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip('\n')
        puzzleinput.append(line)

height = len(puzzleinput)
width = len(puzzleinput[0])

max_height = height + 20
max_width = width + 20

# Create 2D array with 10 spaces either side
grid = numpy.chararray((max_height, max_width),unicode=True)
grid[:] = '.'
# And another to store desired next move locations
nextmovegrid = numpy.zeros((max_height, max_width),numpy.int8)
nextmovegrid = nextmovegrid.reshape(max_height, max_width)

# Create an elf class to store pos and planned next move
class Elf:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.HasMove = False

    def WantsToMove(self, to_y, to_x):
        self.to_y = to_y
        self.to_x = to_x
        self.HasMove = True


# Populate grid
for i in range(0, height, 1):
    for j in range(0, width, 1):
        grid[i+10][j+10] = puzzleinput[i][j]

# Populate elves
elves = []
for y in range(0,max_height):
    for x in range(0, max_width):
        if grid[y][x] == '#':
            elves.append(Elf(y,x))


def printGrid(in_grid, x_min, x_max, y_min, y_max):
    for i in range(y_min, y_max, 1):
        for j in range(x_min, x_max, 1):
            print(in_grid[i][j],end='')
        print()
    print()


#printGrid(grid,0,max_width,0,max_height)

direction_counter = 0

for a in range(0,10):

    # 0 = N, 1 = S, 2 = W, 3 = E
    direction = direction_counter % 4 

    # First half of round - elves decide where to move, or not move
    for elf in elves:
        # Check if all surrounding spaces empty
        if grid[elf.y-1][elf.x-1] == '.' and grid[elf.y][elf.x-1] == '.' and grid[elf.y+1][elf.x-1] == '.' and grid[elf.y+1][elf.x] == '.' and grid[elf.y+1][elf.x+1] == '.' and grid[elf.y][elf.x+1] == '.' and grid[elf.y-1][elf.x+1] == '.' and grid[elf.y-1][elf.x] == '.':
            elf.HasMove = False
        else:
            # Propose moves
            # N S W E
            if direction == 0:
                #North
                if grid[elf.y-1][elf.x-1] == '.' and grid[elf.y-1][elf.x] == '.' and grid[elf.y-1][elf.x+1] == '.':
                    nextmovegrid[elf.y-1][elf.x] += 1
                    elf.WantsToMove(elf.y-1, elf.x)
                #South
                elif grid[elf.y+1][elf.x-1] == '.' and grid[elf.y+1][elf.x] == '.' and grid[elf.y+1][elf.x+1] == '.':
                    nextmovegrid[elf.y+1][elf.x] += 1
                    elf.WantsToMove(elf.y+1, elf.x)
                #West
                elif grid[elf.y-1][elf.x-1] == '.' and grid[elf.y][elf.x-1] == '.' and grid[elf.y+1][elf.x-1] == '.':
                    nextmovegrid[elf.y][elf.x-1] += 1
                    elf.WantsToMove(elf.y, elf.x-1)
                #East
                elif grid[elf.y-1][elf.x+1] == '.' and grid[elf.y][elf.x+1] == '.' and grid[elf.y+1][elf.x+1] == '.':
                    nextmovegrid[elf.y][elf.x+1] += 1
                    elf.WantsToMove(elf.y,elf.x+1)
            # S W E N
            elif direction == 1:
                #South
                if grid[elf.y+1][elf.x-1] == '.' and grid[elf.y+1][elf.x] == '.' and grid[elf.y+1][elf.x+1] == '.':
                    nextmovegrid[elf.y+1][elf.x] += 1
                    elf.WantsToMove(elf.y+1, elf.x)
                #West
                elif grid[elf.y-1][elf.x-1] == '.' and grid[elf.y][elf.x-1] == '.' and grid[elf.y+1][elf.x-1] == '.':
                    nextmovegrid[elf.y][elf.x-1] += 1
                    elf.WantsToMove(elf.y, elf.x-1)
                #East
                elif grid[elf.y-1][elf.x+1] == '.' and grid[elf.y][elf.x+1] == '.' and grid[elf.y+1][elf.x+1] == '.':
                    nextmovegrid[elf.y][elf.x+1] += 1
                    elf.WantsToMove(elf.y,elf.x+1)
                #North
                elif grid[elf.y-1][elf.x-1] == '.' and grid[elf.y-1][elf.x] == '.' and grid[elf.y-1][elf.x+1] == '.':
                    nextmovegrid[elf.y-1][elf.x] += 1
                    elf.WantsToMove(elf.y-1, elf.x)
            # W E N S
            elif direction == 2:
                #West
                if grid[elf.y-1][elf.x-1] == '.' and grid[elf.y][elf.x-1] == '.' and grid[elf.y+1][elf.x-1] == '.':
                    nextmovegrid[elf.y][elf.x-1] += 1
                    elf.WantsToMove(elf.y, elf.x-1)
                #East
                elif grid[elf.y-1][elf.x+1] == '.' and grid[elf.y][elf.x+1] == '.' and grid[elf.y+1][elf.x+1] == '.':
                    nextmovegrid[elf.y][elf.x+1] += 1
                    elf.WantsToMove(elf.y,elf.x+1)
                #North
                elif grid[elf.y-1][elf.x-1] == '.' and grid[elf.y-1][elf.x] == '.' and grid[elf.y-1][elf.x+1] == '.':
                    nextmovegrid[elf.y-1][elf.x] += 1
                    elf.WantsToMove(elf.y-1, elf.x)
                #South
                elif grid[elf.y+1][elf.x-1] == '.' and grid[elf.y+1][elf.x] == '.' and grid[elf.y+1][elf.x+1] == '.':
                    nextmovegrid[elf.y+1][elf.x] += 1
                    elf.WantsToMove(elf.y+1, elf.x)
            # E N S W
            elif direction == 3:
                #East
                if grid[elf.y-1][elf.x+1] == '.' and grid[elf.y][elf.x+1] == '.' and grid[elf.y+1][elf.x+1] == '.':
                    nextmovegrid[elf.y][elf.x+1] += 1
                    elf.WantsToMove(elf.y,elf.x+1)
                #North
                elif grid[elf.y-1][elf.x-1] == '.' and grid[elf.y-1][elf.x] == '.' and grid[elf.y-1][elf.x+1] == '.':
                    nextmovegrid[elf.y-1][elf.x] += 1
                    elf.WantsToMove(elf.y-1, elf.x)
                #South
                elif grid[elf.y+1][elf.x-1] == '.' and grid[elf.y+1][elf.x] == '.' and grid[elf.y+1][elf.x+1] == '.':
                    nextmovegrid[elf.y+1][elf.x] += 1
                    elf.WantsToMove(elf.y+1, elf.x)
                #West
                elif grid[elf.y-1][elf.x-1] == '.' and grid[elf.y][elf.x-1] == '.' and grid[elf.y+1][elf.x-1] == '.':
                    nextmovegrid[elf.y][elf.x-1] += 1
                    elf.WantsToMove(elf.y, elf.x-1)
            else:
                print("Error in direction")

    # Second half of round - do moves if possible
    for elf in elves:
        if elf.HasMove == True:
            # Move elf if possible
            if nextmovegrid[elf.to_y][elf.to_x] == 1:
                grid[elf.y][elf.x] = '.'
                elf.y = elf.to_y
                elf.x = elf.to_x
                grid[elf.y][elf.x] = '#'
                elf.HasMove = False

    # Reset next moves grid
    nextmovegrid[:] = 0

    direction_counter += 1

    #print("Round",direction_counter)
    #printGrid(grid,0,max_width,0,max_height)

# count the number of empty ground tiles contained by the smallest rectangle that contains every Elf.
min_x = 9999
min_y = 9999
max_x = 0
max_y = 0

for elf in elves:
    if elf.y < min_y:
        min_y = elf.y
    if elf.y > max_y:
        max_y = elf.y
    if elf.x < min_x:
        min_x = elf.x
    if elf.x > max_x:
        max_x = elf.x

emptytiles = 0

for y in range(min_y, max_y+1):
    for x in range(min_x, max_x+1):
        if grid[y][x] == '.':
            emptytiles += 1

printGrid(grid,min_x,max_x+1,min_y,max_y+1)
print("Number of empty tiles:",emptytiles)





# Advent of Code 2022 - Puzzle 23-2

import numpy

puzzleinput = []

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip('\n')
        puzzleinput.append(line)

height = len(puzzleinput)
width = len(puzzleinput[0])

max_height = height + 200
max_width = width + 200
 
# Create 2D array with 100 spaces either side (increased for Part 2)
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
        grid[i+100][j+100] = puzzleinput[i][j]

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

# Part 2 - keep track of if any elf moves in a round
elfMoved = True
while elfMoved == True:

    elfMoved = False

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
                elfMoved = True

    # Reset next moves grid
    nextmovegrid[:] = 0

    direction_counter += 1

    #print("Round",direction_counter)
    #printGrid(grid,0,max_width,0,max_height)


print("No moves as of round", direction_counter)


# Advent of Code 2022 - Puzzle 22-1

import numpy

puzzleinput = []
instructions = ''

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        if line.startswith((' ', '.', '#')):
            puzzleinput.append(line)
        else:
            instructions = line

# Get max width of input map
maxwidth = 0
for line in puzzleinput:
    if len(line) > maxwidth:
        maxwidth = len(line)

height = len(puzzleinput)

print("Height:",height)
print("Max width:",maxwidth)

# First, pad out the puzzle input strings where the map ends prior to the max length of any part of the map
for i in range(0, len(puzzleinput)):
    if len(puzzleinput[i]) != maxwidth:
        diff = maxwidth - len(puzzleinput[i])
        for j in range(0, diff):
            puzzleinput[i] += ' '

# Create a list of start and end indices for the .s for every row and column
# Need this to calculating moves from instructions
row_starts = []
row_ends = []
col_starts = []
col_ends = []

for line in puzzleinput:
    start_dots = line.find('.')
    start_hash = line.find('#')

    if start_dots == -1:
        start_dots = 9999
    if start_hash == -1:
        start_hash = 9999

    row_starts.append(min(start_dots, start_hash))
    row_ends.append(max(line.rfind('.'),line.rfind('#')))

for a in range(0, maxwidth):
    start_area = 9999
    end_area = 0
    for b in range(0, height):
        if puzzleinput[b][a] == '.' or puzzleinput[b][a] == '#':
            if b < start_area:
                start_area = b
            if b > end_area:
                end_area = b
    
    col_starts.append(start_area)
    col_ends.append(end_area)

# Set start position
x = puzzleinput[0].find('.')
if x == -1:
    print("Error")
    exit
y = 0
facing = '>'

# Create grid (use ndarray with dtype '<U1' as chararray trims whitespace for some stupid reason)
# See RoboCodoDodo's answer at https://stackoverflow.com/questions/9476797/how-do-i-create-character-arrays-in-numpy
grid = numpy.ndarray((height, maxwidth),dtype='<U1')
grid[:] = ' '

for i in range(0,height):
    for j in range(0,maxwidth):
        grid[i][j] = puzzleinput[i][j]

# Add 'player'
grid[y][x] = facing

def PrintGrid(in_grid, in_height, in_width):
    for i in range(0,in_height):
        for j in range(0,in_width):
            print(in_grid[i][j],end='')
        print()
    print()


# Perform moves
for i in range(0, len(instructions)):
    if instructions[i] == 'R':
        print("Turning right")
        if facing == '>':
            facing = 'V'
        elif facing == 'V':
            facing = '<'
        elif facing == '<':
            facing = '^'
        elif facing == '^':
            facing = '>'
        else:
            print("Error")
    elif instructions[i] == 'L':
        print("Turning left")
        if facing == '>':
            facing = '^'
        elif facing == '^':
            facing = '<'
        elif facing == '<':
            facing = 'V'
        elif facing == 'V':
            facing = '>'
        else:
            print("Error")
    elif str.isdigit(instructions[i]):
        if i < len(instructions) - 1:
            if str.isdigit(instructions[i+1]):
                steps = int(instructions[i] + instructions[i+1])
                print("Moving",steps,"steps")
                for i in range(0, steps):
                    if facing == '>':
                        if x == row_ends[y]:
                            if grid[y][row_starts[y]] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                            elif grid[y][row_starts[y]] == '.':
                                grid[y][x] = '.'
                                x = row_starts[y]
                                grid[y][x] = '>'
                                #PrintGrid(grid, height, maxwidth)
                        else:
                            if grid[y][x+1] == '.':
                                grid[y][x] = '.'
                                x += 1
                                grid[y][x] = '>'
                                #PrintGrid(grid, height, maxwidth)
                            elif grid[y][x+1] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                    elif facing == '<':
                        if x == row_starts[y]:
                            if grid[y][row_ends[y]] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                            elif grid[y][row_ends[y]] == '.':
                                grid[y][x] = '.'
                                x = row_ends[y]
                                grid[y][x] = '<'
                                #PrintGrid(grid, height, maxwidth)
                        else:
                            if grid[y][x-1] == '.':
                                grid[y][x] = '.'
                                x -= 1
                                grid[y][x] = '<'
                                #PrintGrid(grid, height, maxwidth)
                            elif grid[y][x-1] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                    elif facing == 'V':
                        if y == col_ends[x]:
                            if grid[col_starts[x]][x] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                            elif grid[col_starts[x]][x] == '.':
                                print("y",y,"x",x,"cs",col_starts[x])
                                grid[y][x] = '.'
                                y = col_starts[x]
                                grid[y][x] = 'V'
                                #PrintGrid(grid, height, maxwidth)
                        else:
                            if grid[y+1][x] == '.':
                                grid[y][x] = '.'
                                y += 1
                                grid[y][x] = 'v'
                                #PrintGrid(grid, height, maxwidth)
                            elif grid[y+1][x] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                    elif facing == '^':
                        if y == col_starts[x]:
                            if grid[col_ends[x]][x] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                            elif grid[col_ends[x]][x] == '.':
                                grid[y][x] = '.'
                                y = col_ends[x]
                                grid[y][x] = '^'
                                #PrintGrid(grid, height, maxwidth)
                        else:
                            if grid[y-1][x] == '.':
                                grid[y][x] = '.'
                                y -= 1
                                grid[y][x] = '^'
                                #PrintGrid(grid, height, maxwidth)
                            elif grid[y-1][x] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                    
            elif str.isdigit(instructions[i-1]):
                continue
            else:
                steps = int(instructions[i])
                print("Moving",steps,"steps")
                for i in range(0, steps):
                    if facing == '>':
                        if x == row_ends[y]:
                            if grid[y][row_starts[y]] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                            elif grid[y][row_starts[y]] == '.':
                                grid[y][x] = '.'
                                x = row_starts[y]
                                grid[y][x] = '>'
                                #PrintGrid(grid, height, maxwidth)
                        else:
                            if grid[y][x+1] == '.':
                                grid[y][x] = '.'
                                x += 1
                                grid[y][x] = '>'
                                #PrintGrid(grid, height, maxwidth)
                            elif grid[y][x+1] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                    elif facing == '<':
                        if x == row_starts[y]:
                            if grid[y][row_ends[y]] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                            elif grid[y][row_ends[y]] == '.':
                                grid[y][x] = '.'
                                x = row_ends[y]
                                grid[y][x] = '<'
                                #PrintGrid(grid, height, maxwidth)
                        else:
                            if grid[y][x-1] == '.':
                                grid[y][x] = '.'
                                x -= 1
                                grid[y][x] = '<'
                                #PrintGrid(grid, height, maxwidth)
                            elif grid[y][x-1] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                    elif facing == 'V':
                        if y == col_ends[x]:
                            if grid[col_starts[x]][x] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                            elif grid[col_starts[x]][x] == '.':
                                grid[y][x] = '.'
                                y = col_starts[x]
                                grid[y][x] = 'V'
                                #PrintGrid(grid, height, maxwidth)
                        else:
                            if grid[y+1][x] == '.':
                                grid[y][x] = '.'
                                y += 1
                                grid[y][x] = 'v'
                                #PrintGrid(grid, height, maxwidth)
                            elif grid[y+1][x] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                    elif facing == '^':
                        if y == col_starts[x]:
                            if grid[col_ends[x]][x] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                            elif grid[col_ends[x]][x] == '.':
                                grid[y][x] = '.'
                                y = col_ends[x]
                                grid[y][x] = '^'
                                #PrintGrid(grid, height, maxwidth)
                        else:
                            if grid[y-1][x] == '.':
                                grid[y][x] = '.'
                                y -= 1
                                grid[y][x] = '^'
                                #PrintGrid(grid, height, maxwidth)
                            elif grid[y-1][x] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
        else:
            if str.isdigit(instructions[i-1]):
                continue
            else:
                steps = int(instructions[i])
                print("Moving",steps,"steps")
                for i in range(0, steps):
                    if facing == '>':
                        if x == row_ends[y]:
                            if grid[y][row_starts[y]] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                            elif grid[y][row_starts[y]] == '.':
                                grid[y][x] = '.'
                                x = row_starts[y]
                                grid[y][x] = '>'
                                #PrintGrid(grid, height, maxwidth)
                        else:
                            if grid[y][x+1] == '.':
                                grid[y][x] = '.'
                                x += 1
                                grid[y][x] = '>'
                                #PrintGrid(grid, height, maxwidth)
                            elif grid[y][x+1] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                    elif facing == '<':
                        if x == row_starts[y]:
                            if grid[y][row_ends[y]] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                            elif grid[y][row_ends[y]] == '.':
                                grid[y][x] = '.'
                                x = row_ends[y]
                                grid[y][x] = '<'
                                #PrintGrid(grid, height, maxwidth)
                        else:
                            if grid[y][x-1] == '.':
                                grid[y][x] = '.'
                                x -= 1
                                grid[y][x] = '<'
                                #PrintGrid(grid, height, maxwidth)
                            elif grid[y][x-1] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                    elif facing == 'V':
                        if y == col_ends[x]:
                            if grid[col_starts[x]][x] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                            elif grid[col_starts[x]][x] == '.':
                                grid[y][x] = '.'
                                y = col_starts[x]
                                grid[y][x] = 'V'
                                #PrintGrid(grid, height, maxwidth)
                        else:
                            if grid[y+1][x] == '.':
                                grid[y][x] = '.'
                                y += 1
                                grid[y][x] = 'v'
                                #PrintGrid(grid, height, maxwidth)
                            elif grid[y+1][x] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                    elif facing == '^':
                        if y == col_starts[x]:
                            if grid[col_ends[x]][x] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break
                            elif grid[col_ends[x]][x] == '.':
                                grid[y][x] = '.'
                                y = col_ends[x]
                                grid[y][x] = '^'
                                #PrintGrid(grid, height, maxwidth)
                        else:
                            if grid[y-1][x] == '.':
                                grid[y][x] = '.'
                                y -= 1
                                grid[y][x] = '^'
                                #PrintGrid(grid, height, maxwidth)
                            elif grid[y-1][x] == '#':
                                print("Can't move further")
                                #PrintGrid(grid, height, maxwidth)
                                break

grid[y][x] = facing

print("Final state")
PrintGrid(grid, height, maxwidth)

# To finish providing the password to this strange input device, you need to determine numbers for your final row, column, and facing 
# as your final position appears from the perspective of the original map.
# Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^). The final password is the sum of 1000 times the row, 4 times the column, and the facing.
if facing == '>':
    facing_value = 0
elif facing == 'V':
    facing_value = 1
elif facing == '<':
    facing_value = 2
elif facing == '^':
    facing_value = 3

password = (1000 * (y+1)) + (4 * (x+1)) + facing_value
print("Password is",password)
# Advent of Code 2022 - Puzzle 8-1

puzzleinput = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        puzzleinput.append(line)

height = len(puzzleinput)
length = len(puzzleinput[0])

forest = []

for line in puzzleinput:
    line_list = list(line)
    forest.append(line_list)

# Edge squares formula, always visible
initially_visible = (length - 1) * 4

num_visible = initially_visible

# Iterate over every non-edge tree and check visibility in vert/hor directions, continuing loop early if a visible direction is found
for x in range(1,length-1):
    for y in range(1,height-1):
        visible = True

        # Check north
        for n_x in range(1, x+1):
            if forest[x - n_x][y] >= forest[x][y]:
                visible = False
                break


        if visible == True:
            num_visible += 1
            continue
        else:
            visible = True


        # Check south
        for n_x in range(1, height - x):
            if forest[x + n_x][y] >= forest[x][y]:
                visible = False
                break

        if visible == True:
            num_visible += 1
            continue
        else:
            visible = True

        # Check west
        for n_y in range(1, y+1):
            if forest[x][y - n_y] >= forest[x][y]:
                visible = False
                break

        if visible == True:
            num_visible += 1
            continue
        else:
            visible = True

        # Check east
        for n_y in range(1, length - y):
            if forest[x][y + n_y] >= forest[x][y]:
                visible = False
                break
    
        if visible == True:
            num_visible += 1
        

print("Total visible trees: ", num_visible)

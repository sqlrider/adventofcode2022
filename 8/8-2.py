# Advent of Code 2022 - Puzzle 8-2

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

highest_scenic_score = 0

for x in range(1,length-1):
    for y in range(1,height-1):

        # For part 2, can't short-circuit the loop when finding a visible tree as need to calc scenic score,
        # so need to track visibility for each direction then check at end of loop
        n_visible = True
        s_visible = True
        w_visible = True
        e_visible = True

        view_dist_north = 0
        view_dist_south = 0
        view_dist_west = 0
        view_dist_east = 0

        # Check north
        for n_x in range(1, x+1):
            view_dist_north += 1
            if forest[x - n_x][y] >= forest[x][y]:
                n_visible = False
                break

        # Check south
        for n_x in range(1, height - x):
            view_dist_south += 1
            if forest[x + n_x][y] >= forest[x][y]:
                s_visible = False
                break

        # Check west
        for n_y in range(1, y+1):
            view_dist_west += 1
            if forest[x][y - n_y] >= forest[x][y]:
                w_visible = False
                break

        # Check east
        for n_y in range(1, length - y):
            view_dist_east += 1
            if forest[x][y + n_y] >= forest[x][y]:
                e_visible = False
                break
    
        if n_visible == True or s_visible == True or w_visible == True or e_visible == True:
            num_visible += 1
            scenic_score = view_dist_north * view_dist_south * view_dist_west * view_dist_east
            # print("At ",forest[x][y],", scenic score: ",scenic_score, "North:",view_dist_north, ", South:", view_dist_south,", West:",view_dist_west,", East:", view_dist_east)

            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score

print("Highest scenic score: ", highest_scenic_score)

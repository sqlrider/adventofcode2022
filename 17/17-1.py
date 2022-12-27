# Advent of Code 2022 - Puzzle 17-1

import numpy
import time

puzzleinput = ""

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip('\n')
        puzzleinput = line

# Create array for empty space + 1 each side to save for bounds checking for block movement
tetris = numpy.chararray((8000,9), unicode=True)
tetris[:] = '-'
for a in range(1,9):
    tetris[0][a] = '*'
for a in range(0,5000):
    tetris[a][0] = '|'
    tetris[a][8] = '|'

def PrintTetris(in_tetris, y_min, y_max):
    for i in range(y_max, y_min -1, -1):
        for j in range (0,9):
            print(tetris[i][j],end='')
        print()
    print()


debug = False
highest_rock_level = 0

blocks_falling = True

wind_counter = 0
wind_incr = 0

block_type = 0
block_incr = 0

while(blocks_falling):
    
    block_type = block_incr % 5
    
    # ####
    if block_type == 0:
        # Add block to starting position
        tetris[highest_rock_level + 4][3] = '#'
        tetris[highest_rock_level + 4][4] = '#'
        tetris[highest_rock_level + 4][5] = '#'
        tetris[highest_rock_level + 4][6] = '#'

        root_pos_x = 3
        root_pos_y = highest_rock_level + 4

        
        if debug:
            print("Block added")
            PrintTetris(tetris,0,20)

        # Blockfall
        current_block_at_rest = False
        while(not current_block_at_rest):

            wind_counter = wind_incr % len(puzzleinput)

            # Move block from wind
            if puzzleinput[wind_counter] == '<':           
                if tetris[root_pos_y][root_pos_x - 1] == '-':
                    tetris[root_pos_y][root_pos_x -1] = '#'
                    tetris[root_pos_y][root_pos_x + 3] = '-'
                    root_pos_x -= 1

            elif puzzleinput[wind_counter] == '>':
                if tetris[root_pos_y][root_pos_x + 4] == '-':
                    tetris[root_pos_y][root_pos_x + 4] = '#'
                    tetris[root_pos_y][root_pos_x] = '-'
                    root_pos_x += 1

            # Drop block if space below clear
            if tetris[root_pos_y - 1][root_pos_x] == '-' and tetris[root_pos_y - 1][root_pos_x + 1] == '-' and tetris[root_pos_y - 1][root_pos_x + 2] == '-' and tetris[root_pos_y - 1][root_pos_x + 3] == '-':
                tetris[root_pos_y -1][root_pos_x] = '#'
                tetris[root_pos_y -1][root_pos_x + 1] = '#'
                tetris[root_pos_y -1][root_pos_x + 2] = '#'
                tetris[root_pos_y -1][root_pos_x + 3] = '#'

                tetris[root_pos_y][root_pos_x] = '-'
                tetris[root_pos_y][root_pos_x + 1] = '-'
                tetris[root_pos_y][root_pos_x + 2] = '-'
                tetris[root_pos_y][root_pos_x + 3] = '-'

                root_pos_y -= 1
            else:
                current_block_at_rest = True
                if root_pos_y > highest_rock_level:
                    highest_rock_level = root_pos_y

            if debug:
                print("Block dropped")
                PrintTetris(tetris,0,20)

            wind_incr += 1

    # .#.
    # ###
    # .#.
    if block_type == 1:
        # Add block to starting position
        tetris[highest_rock_level + 5][3] = '#'
        tetris[highest_rock_level + 5][4] = '#'
        tetris[highest_rock_level + 5][5] = '#'
        tetris[highest_rock_level + 4][4] = '#'
        tetris[highest_rock_level + 6][4] = '#'

        root_pos_x = 3
        root_pos_y = highest_rock_level + 4

        
        if debug:
            print("Block added")
            PrintTetris(tetris,0,20)

        # Blockfall
        current_block_at_rest = False
        while(not current_block_at_rest):

            wind_counter = wind_incr % len(puzzleinput)

            # Move block from wind
            if puzzleinput[wind_counter] == '<':           
                if tetris[root_pos_y + 1][root_pos_x - 1] == '-' and tetris[root_pos_y][root_pos_x] == '-' and tetris[root_pos_y + 2][root_pos_x] == '-':
                    tetris[root_pos_y][root_pos_x] = '#'
                    tetris[root_pos_y + 1][root_pos_x - 1] = '#'
                    tetris[root_pos_y + 2][root_pos_x] = '#'
                    
                    tetris[root_pos_y][root_pos_x + 1] = '-'
                    tetris[root_pos_y + 1][root_pos_x + 2] = '-'
                    tetris[root_pos_y + 2][root_pos_x + 1] = '-'
                    root_pos_x -= 1

            elif puzzleinput[wind_counter] == '>':
                if tetris[root_pos_y + 1][root_pos_x + 3] == '-' and tetris[root_pos_y][root_pos_x + 2] == '-' and tetris[root_pos_y + 2][root_pos_x + 2] == '-':
                    tetris[root_pos_y][root_pos_x + 2] = '#'
                    tetris[root_pos_y + 1][root_pos_x + 3] = '#'
                    tetris[root_pos_y + 2][root_pos_x + 2] = '#'
                    
                    tetris[root_pos_y][root_pos_x + 1] = '-'
                    tetris[root_pos_y + 1][root_pos_x] = '-'
                    tetris[root_pos_y + 2][root_pos_x + 1] = '-'
                    root_pos_x += 1

            # Drop block if space below clear
            if tetris[root_pos_y][root_pos_x] == '-' and tetris[root_pos_y - 1][root_pos_x + 1] == '-' and tetris[root_pos_y][root_pos_x + 2] == '-':
                tetris[root_pos_y][root_pos_x] = '#'
                tetris[root_pos_y][root_pos_x + 2] = '#'
                tetris[root_pos_y -1][root_pos_x + 1] = '#'

                tetris[root_pos_y + 1][root_pos_x] = '-'
                tetris[root_pos_y + 1][root_pos_x + 2] = '-'
                tetris[root_pos_y + 2][root_pos_x + 1] = '-'              

                root_pos_y -= 1
            else:
                current_block_at_rest = True
                if root_pos_y + 2 > highest_rock_level:
                    highest_rock_level = root_pos_y + 2

            if debug:
                print("Block dropped")
                PrintTetris(tetris,0,20)

            wind_incr += 1
    ### End block

    # ..#
    # ..#
    # ###
    if block_type == 2:
        # Add block to starting position
        tetris[highest_rock_level + 4][3] = '#'
        tetris[highest_rock_level + 4][4] = '#'
        tetris[highest_rock_level + 4][5] = '#'
        tetris[highest_rock_level + 5][5] = '#'
        tetris[highest_rock_level + 6][5] = '#'

        root_pos_x = 3
        root_pos_y = highest_rock_level + 4

        if debug:
            print("Block added")
            PrintTetris(tetris,0,20)

        # Blockfall
        current_block_at_rest = False
        while(not current_block_at_rest):

            wind_counter = wind_incr % len(puzzleinput)

            # Move block from wind
            if puzzleinput[wind_counter] == '<':           
                if tetris[root_pos_y][root_pos_x - 1] == '-' and tetris[root_pos_y + 1][root_pos_x + 1] == '-' and tetris[root_pos_y + 2][root_pos_x + 1] == '-':
                    tetris[root_pos_y][root_pos_x - 1] = '#'
                    tetris[root_pos_y + 1][root_pos_x + 1] = '#'
                    tetris[root_pos_y + 2][root_pos_x + 1] = '#'

                    tetris[root_pos_y][root_pos_x + 2] = '-'
                    tetris[root_pos_y + 1][root_pos_x + 2] = '-'
                    tetris[root_pos_y + 2][root_pos_x + 2] = '-'
                    root_pos_x -= 1

            elif puzzleinput[wind_counter] == '>':
                if tetris[root_pos_y][root_pos_x + 3] == '-' and tetris[root_pos_y + 1][root_pos_x + 3] == '-' and tetris[root_pos_y + 2][root_pos_x + 3] == '-':
                    tetris[root_pos_y][root_pos_x + 3] = '#'
                    tetris[root_pos_y + 1][root_pos_x + 3] = '#'
                    tetris[root_pos_y + 2][root_pos_x + 3] = '#'

                    tetris[root_pos_y][root_pos_x] = '-'
                    tetris[root_pos_y+1][root_pos_x+2] = '-'
                    tetris[root_pos_y+2][root_pos_x+2] = '-'
                    root_pos_x += 1

            # Drop block if space below clear
            if tetris[root_pos_y - 1][root_pos_x] == '-' and tetris[root_pos_y - 1][root_pos_x + 1] == '-' and tetris[root_pos_y - 1][root_pos_x + 2] == '-':
                tetris[root_pos_y - 1][root_pos_x] = '#'
                tetris[root_pos_y - 1][root_pos_x + 1] = '#'
                tetris[root_pos_y - 1][root_pos_x + 2] = '#'

                tetris[root_pos_y][root_pos_x] = '-'
                tetris[root_pos_y][root_pos_x + 1] = '-'
                tetris[root_pos_y + 2][root_pos_x + 2] = '-'              

                root_pos_y -= 1
            else:
                current_block_at_rest = True
                if root_pos_y + 2 > highest_rock_level:
                    highest_rock_level = root_pos_y + 2

            if debug:
                print("Blocked dropped")
                PrintTetris(tetris,0,20)

            wind_incr += 1
    ### End block

    # #
    # #
    # #
    # #
    if block_type == 3:
        # Add block to starting position
        tetris[highest_rock_level + 4][3] = '#'
        tetris[highest_rock_level + 5][3] = '#'
        tetris[highest_rock_level + 6][3] = '#'
        tetris[highest_rock_level + 7][3] = '#'

        root_pos_x = 3
        root_pos_y = highest_rock_level + 4

        if debug:
            print("Block added")
            PrintTetris(tetris,0,20)

        # Blockfall
        current_block_at_rest = False
        while(not current_block_at_rest):

            wind_counter = wind_incr % len(puzzleinput)

            # Move block from wind
            if puzzleinput[wind_counter] == '<':           
                if tetris[root_pos_y][root_pos_x - 1] == '-' and tetris[root_pos_y + 1][root_pos_x - 1] == '-' and tetris[root_pos_y+2][root_pos_x - 1] == '-' and tetris[root_pos_y+3][root_pos_x - 1] == '-':
                    tetris[root_pos_y][root_pos_x-1] = '#'
                    tetris[root_pos_y+1][root_pos_x-1] = '#'
                    tetris[root_pos_y+2][root_pos_x-1] = '#'
                    tetris[root_pos_y+3][root_pos_x-1] = '#'

                    tetris[root_pos_y][root_pos_x] = '-'
                    tetris[root_pos_y+1][root_pos_x] = '-'
                    tetris[root_pos_y+2][root_pos_x] = '-'
                    tetris[root_pos_y+3][root_pos_x] = '-'

                    root_pos_x -= 1

            elif puzzleinput[wind_counter] == '>':
                if tetris[root_pos_y][root_pos_x+1] == '-' and tetris[root_pos_y+1][root_pos_x+1] == '-' and tetris[root_pos_y+2][root_pos_x+1] == '-' and tetris[root_pos_y+3][root_pos_x+1] == '-':
                    tetris[root_pos_y][root_pos_x+1] = '#'
                    tetris[root_pos_y+1][root_pos_x+1] = '#'
                    tetris[root_pos_y+2][root_pos_x+1] = '#'
                    tetris[root_pos_y+3][root_pos_x+1] = '#'

                    tetris[root_pos_y][root_pos_x] = '-'
                    tetris[root_pos_y+1][root_pos_x] = '-'
                    tetris[root_pos_y+2][root_pos_x] = '-'
                    tetris[root_pos_y+3][root_pos_x] = '-'

                    root_pos_x += 1


            # Drop block if space below clear
            if tetris[root_pos_y-1][root_pos_x] == '-':
                    tetris[root_pos_y-1][root_pos_x] = '#'

                    tetris[root_pos_y+3][root_pos_x] = '-'           

                    root_pos_y -= 1
            else:
                current_block_at_rest = True
                if root_pos_y + 3 > highest_rock_level:
                    highest_rock_level = root_pos_y + 3

            if debug:
                print("Block dropped")
                PrintTetris(tetris,0,20)

            wind_incr += 1
    
    ### End block

    # ##
    # ##
    if block_type == 4:
        # Add block to starting position
        tetris[highest_rock_level + 4][3] = '#'
        tetris[highest_rock_level + 5][3] = '#'
        tetris[highest_rock_level + 4][4] = '#'
        tetris[highest_rock_level + 5][4] = '#'

        root_pos_x = 3
        root_pos_y = highest_rock_level + 4

        if debug:
            print("Block added")
            PrintTetris(tetris,0,20)

        # Blockfall
        current_block_at_rest = False
        while(not current_block_at_rest):

            wind_counter = wind_incr % len(puzzleinput)

            # Move block from wind
            if puzzleinput[wind_counter] == '<':           
                if tetris[root_pos_y][root_pos_x-1] == '-' and tetris[root_pos_y+1][root_pos_x-1] == '-':
                    tetris[root_pos_y][root_pos_x-1] = '#'
                    tetris[root_pos_y+1][root_pos_x-1] = '#'

                    tetris[root_pos_y][root_pos_x+1] = '-'
                    tetris[root_pos_y+1][root_pos_x+1] = '-'

                    root_pos_x -= 1

            elif puzzleinput[wind_counter] == '>':
                if tetris[root_pos_y][root_pos_x+2] == '-' and tetris[root_pos_y+1][root_pos_x+2] == '-':
                    tetris[root_pos_y][root_pos_x+2] = '#'
                    tetris[root_pos_y+1][root_pos_x+2] = '#'

                    tetris[root_pos_y][root_pos_x] = '-'
                    tetris[root_pos_y+1][root_pos_x] = '-'

                    root_pos_x += 1

            # Drop block if space below clear
            if tetris[root_pos_y-1][root_pos_x] == '-' and tetris[root_pos_y-1][root_pos_x+1] == '-':
                    tetris[root_pos_y-1][root_pos_x] = '#'
                    tetris[root_pos_y-1][root_pos_x+1] = '#'

                    tetris[root_pos_y+1][root_pos_x] = '-'
                    tetris[root_pos_y+1][root_pos_x+1] = '-'        

                    root_pos_y -= 1
            else:
                current_block_at_rest = True
                if root_pos_y + 1 > highest_rock_level:
                    highest_rock_level = root_pos_y + 1

            if debug:
                print("Block dropped")
                PrintTetris(tetris,0,20)

            wind_incr += 1
    
    ### End block

    block_incr += 1

    if block_incr == 2022:
        blocks_falling = False


print("Height:",highest_rock_level)
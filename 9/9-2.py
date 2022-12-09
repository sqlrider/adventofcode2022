# Advent of Code 2022 - Puzzle 9-2

puzzleinput = []

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip('\n')
        puzzleinput.append(line)

# For part 10, treat as ten knots not a head and tail(s)
knot_pos = []
for i in range(0,10):
    knot_pos.append(dict({'x': 0, 'y': 0}))

visited_positions = []
visited_positions.append((0,0))

for line in puzzleinput:
    direction = line.split(" ")[0]
    steps = int(line.split(" ")[1])

    # Move the head first
    # print("Moving", steps,direction)
    for j in range(1,steps+1):
        if direction == 'D':
            knot_pos[0]['y'] -= 1
        elif direction == 'U':
            knot_pos[0]['y'] += 1
        elif direction == 'L':
            knot_pos[0]['x'] -= 1
        elif direction == 'R':
            knot_pos[0]['x'] += 1

        # for each knot besides the head
        for i in range(1, 10):

            # For part 2, can't use logic of tail = last_head_pos or even a last_tail_pos equivalent, as the physics are different.
            # Now need to treat this as a maths problem as calculate the 'pull' effect of the knots moving

            # Calculate relative and absolute x and y distance between current and prior knot
            dx = knot_pos[i-1]['x'] - knot_pos[i]['x']
            abs_dx = abs(dx)
            dy = knot_pos[i-1]['y'] - knot_pos[i]['y']
            abs_dy = abs(dy)

            # First check if any move is required 
            if abs_dx > 1 or abs_dy > 1:
                # Need to move horizontally
                if abs_dx > 1:  
                    if dx > 0:
                        knot_pos[i]['x'] += 1
                    elif dx < 0:
                        knot_pos[i]['x'] -= 1
                    # Also move vertically if not aligned
                    if abs_dy == 1:
                        if dy > 0:
                            knot_pos[i]['y'] += 1
                        elif dy < 0:
                            knot_pos[i]['y'] -= 1
                # Need to move vertically
                if abs_dy > 1:  
                    if dy > 0:
                        knot_pos[i]['y'] += 1
                    elif dy < 0:
                        knot_pos[i]['y'] -= 1
                    # Also move horizontally if not aligned
                    if abs_dx == 1:
                        if dx > 0:
                            knot_pos[i]['x'] += 1
                        elif dx < 0:
                            knot_pos[i]['x'] -= 1

                #print("Moved knot",i, "to",knot_pos[i]['x'],",",knot_pos[i]['y'])

        str_pos = (knot_pos[9]['x'],knot_pos[9]['y'])
        visited_positions.append(str_pos)

print("Visited positions:", len(visited_positions))
print("Unique visited positions:",len(set(visited_positions)))

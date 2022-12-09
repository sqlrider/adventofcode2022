# Advent of Code 2022 - Puzzle 9-1

puzzleinput = []

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip('\n')
        puzzleinput.append(line)

H_pos = dict({'x': 0, 'y': 0})
T_pos = dict({'x': 0, 'y': 0})
last_H_pos = dict({'x': 0, 'y': 0})

visited_positions = []
visited_positions.append("0,0")

for line in puzzleinput:
    direction = line.split(" ")[0]
    steps = int(line.split(" ")[1])

    # print("Moving", steps,direction)
    # Move the head
    for i in range(1,steps+1):
        if direction == 'D':
            H_pos['y'] -= 1
        elif direction == 'U':
            H_pos['y'] += 1
        elif direction == 'L':
            H_pos['x'] -= 1
        elif direction == 'R':
            H_pos['x'] += 1

        # Move the tail if it needs to move by checking absolute change in x or y 
        if abs(H_pos['x'] - T_pos['x']) > 1 or abs(H_pos['y'] - T_pos['y']) > 1:
            # If it moves, it takes the position the head was in previously
            T_pos['x'] = last_H_pos['x']
            T_pos['y'] = last_H_pos['y']
            str_pos = (T_pos['x'],T_pos['y'])
            visited_positions.append(str_pos)

        last_H_pos['x'] = H_pos['x']
        last_H_pos['y'] = H_pos['y']

print("Visited positions:", len(visited_positions))
print("Unique visited positions:",len(set(visited_positions)))

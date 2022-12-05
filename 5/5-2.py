# Advent of Code 2022 - Puzzle 5-2

puzzleinput = []

with open('input.txt', 'r') as file:
    for line in file:
        puzzleinput.append(line)

stack_list = 0

# Find line in input that contains numbers of stacks, also functions as divider for layout / instructions
for index, line in enumerate(puzzleinput):
    if line.startswith(' 1'):
        stack_list = index

number_of_stacks = max(list(map(int,puzzleinput[stack_list].strip().split())))

# Initialise list of stacks as can't index into undeclared list member
stacks = []
for i in range(0, number_of_stacks):
    stacks.append([])

# Need to read input upwards from stack_list for stack_list lines
for x in range(stack_list -1, -1, -1):
    # Now need to add any non-empty stack values based on offset - [2], [6], [10]
    # y * 4 + 1
    for y in range(0, number_of_stacks):
        if puzzleinput[x][(y*4)+1] != ' ':
            stacks[y].append(puzzleinput[x][(y*4)+1])

for i in range(stack_list+2, len(puzzleinput), 1):
    instructions = puzzleinput[i].strip().split(' ')
    move_value = int(instructions[1])
    from_value = int(instructions[3]) - 1
    to_value = int(instructions[5]) - 1

    # Part 2 - need to pop to an intermediate stack and append in reverse order
    intermediate = []

    for j in range(0, move_value):
        intermediate.append(stacks[from_value].pop())

    for j in range(move_value, 0, -1):
        stacks[to_value].append(intermediate[j-1])
        
# Assemble final string from top of each stack
topcrates = ''

for stack in stacks:
    topcrates += stack.pop()

print(topcrates)

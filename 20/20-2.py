# Advent of Code 2022 - Puzzle 20-2

from collections import deque

puzzleinput = []

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip('\n')
        puzzleinput.append(line)

list_size = len(puzzleinput)

# Part 2 - First, you need to apply the decryption key, 811589153.
# Multiply each number by the decryption key before you begin; this will produce the actual list of numbers to mix.

# Make copy of list of numbers/indices to keep ordering
original_list = []
i = 0
for line in puzzleinput:
    original_list.append((i, int(line) * 811589153))
    if int(line) == 0:      # Store original position of zero seperately for later
        zero_pos = (i, 0)
    i += 1


# Populate double ended queue to use rotation functionality 
puzzle = deque()
i = 0
for line in puzzleinput:
    puzzle.append((i, int(line) * 811589153))
    i += 1

# Part 2 - Second, you need to mix the list of numbers ten times.
for n in range(0, 10):

    for a in range(0, len(original_list)):

        # Remove tuple from left of list, then rotate deque by it's value mod list size -1 (-1 because just taken an item out of queue), then append item back to left of deque
        tmp = puzzle.popleft()
        rotate = tmp[1] % (list_size - 1)

        puzzle.rotate(-rotate)

        puzzle.appendleft(tmp)

        # Get the deque index of the next number/index pair needed to rotate, then rotate by the index value to bring that tuple to the 'left' side of the deque
        if a < len(original_list) - 1:
            next_index = puzzle.index(original_list[a+1])      
            puzzle.rotate(-next_index)
        else:
            # Part 2 - reset queue to first index position, ready for next iteration of 'mixing'
            start_index = puzzle.index(original_list[0])
            puzzle.rotate(-start_index)

# Reset to 0 at left end of deque on last iteration, using index of 0 value captured earlier
zero_index = puzzle.index(zero_pos)
puzzle.rotate(-zero_index)


# Sum values at the 1000th, 2000th, and 3000th numbers after the value 0, wrapping around the list as necessary.
rotate = 1000 % (list_size)
puzzle.rotate(-rotate)
n1 = puzzle[0][1]
puzzle.rotate(-rotate)
n2 = puzzle[0][1]
puzzle.rotate(-rotate)
n3 = puzzle[0][1]

coords = n1 + n2 + n3
print("n1:",n1,"n2:",n2,"n3:",n3,"coords:",coords)
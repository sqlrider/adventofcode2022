# # Advent of Code 2022 - Puzzle 13-2

import math

puzzleinput = []

# Part 2 - "Now, you just need to put all of the packets in the right order. Disregard the blank lines in your list of received packets.""
with open("input.txt", 'r') as file:
    for line in file:
        if line != '\n':
            puzzleinput.append(line.strip('\n'))

# The distress signal protocol also requires that you include two additional divider packets:
# [[2]]
# [[6]]
puzzleinput.append('[[2]]')
puzzleinput.append('[[6]]')

#print(puzzleinput)

# Build a recursive comparison function.
# Need to check whether l/r values are ints or lists - recurse if lists, compare if ints/list lengths - and bubble up either 0 or 1 values for in order vs out of order, as 
# logic for orderedness is short-circuitable so can return as soon as a valid result is found
def compare(left, right):
    # If both values are ints, just do simple integer comparison. Return 0 if in order, 1 if not, and don't return anything if both ints are equal.
    if isinstance(left, int) and isinstance(right,int):
        if left < right:
            return 0
        elif right < left:
            return 1
    # Else if both values are lists, then iterate over them i times where i is the length of smaller list
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(0, min(len(left), len(right))):
            result = compare(left[i], right[i])
            if result == 1:
                return 1
            elif result == 0:
                return 0
        # If loop finishes and code hasn't returned, means list is still in order and we're still checking, next check
        # is which list runs out of values first
        if len(left) < len(right):
            return 0
        elif len(right) < len(left):
            return 1
    # If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison.
    elif isinstance(left, int) and isinstance(right, list):
        lefttmp = []
        lefttmp.append(left)
        left = lefttmp
        result = compare(left, right)
        if result == 1:
            return 1
        elif result == 0:
            return 0
    elif isinstance(left, list) and isinstance(right, int):
        righttmp = []
        righttmp.append(right)
        right = righttmp
        result = compare(left, right)
        if result == 1:
            return 1
        elif result == 0:
            return 0

index = 0
indices = 0

# Part 2 - do a bubble sort to sort list
still_sorting = True

while(still_sorting):

    still_sorting = False

    for n in range(0,len(puzzleinput) - 1):

        a = eval(puzzleinput[n])
        b = eval(puzzleinput[n+1])

        result = compare(a, b)
        
        # If not in order, swap
        if result == 1:
            tmp = puzzleinput[n]
            puzzleinput[n] = puzzleinput[n+1]
            puzzleinput[n+1] = tmp
            still_sorting = True
            
print("Sort complete")
for line in puzzleinput:
    print(line)

decoder_key = 1

# "To find the decoder key for this distress signal, you need to determine the indices of the two divider packets and multiply them together"
for i in range(0,len(puzzleinput)):
    if puzzleinput[i] == '[[2]]' or puzzleinput[i] == '[[6]]':
        print("Found divider at index", i+1)
        decoder_key *= i+1

print("Decoder key:",decoder_key)

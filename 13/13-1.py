# # Advent of Code 2022 - Puzzle 13-1

import math

puzzleinput = []

with open("input.txt", 'r') as file:
    for line in file:
        puzzleinput.append(line.strip('\n'))

# Build a recursive comparison function.
# Need to check whether l/r values are ints or lists - recurse if lists, compare if ints/list lengths - and bubble up either 0 or 1 values for in order vs out of order, as 
# logic for orderedness is short-circuitable so can return as soon as a valid result is found
def compare(left, right):
    # If both values are ints, just do simple integer comparison. Return 0 if in order, 1 if not, and don't return anything if both ints are equal.
    if isinstance(left, int) and isinstance(right,int):
        print("Comparing ints",left,"vs", right)
        if left < right:
            print("Integer check success, returning 0")
            return 0
        elif right < left:
            print("Integer check failed, returning 1")
            return 1
    # Else if both values are lists, then iterate over them i times where i is the length of smaller list
    elif isinstance(left, list) and isinstance(right, list):
        print("Comparing lists", left, "vs", right)
        for i in range(0, min(len(left), len(right))):
            result = compare(left[i], right[i])
            if result == 1:
                print("List not in order, returning 1")
                return 1
            elif result == 0:
                print("List in order, returning 0")
                return 0
        # If loop finishes and code hasn't returned, means list is still in order and we're still checking, next check
        # is which list runs out of values first
        print("Comparing length",left,"vs",right)
        if len(left) < len(right):
            print("Length check success, returning 0")
            return 0
        elif len(right) < len(left):
            print("Length check failed, returning 1")
            return 1
    # If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison.
    elif isinstance(left, int) and isinstance(right, list):
        lefttmp = []
        lefttmp.append(left)
        left = lefttmp
        result = compare(left, right)
        if result == 1:
            print("List not in order, returning 1")
            return 1
        elif result == 0:
            print("List in order, returning 0")
            return 0
    elif isinstance(left, list) and isinstance(right, int):
        righttmp = []
        righttmp.append(right)
        right = righttmp
        result = compare(left, right)
        if result == 1:
            print("List not in order, returning 1")
            return 1
        elif result == 0:
            print("List in order, returning 0")
            return 0

index = 0
indices = 0

for n in range(0,len(puzzleinput), 3):
    
    index += 1

    a = eval(puzzleinput[n])
    b = eval(puzzleinput[n+1])

    result = compare(a, b)
    if result == 0:
        print("Lists in correct order")
        indices += index
    else:
        print("Lists not in correct order")

print("Sum of correct indices:",indices)
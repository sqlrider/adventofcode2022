# Advent of Code 2022 - Puzzle 10-1

puzzleinput = []

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip('\n')
        puzzleinput.append(line.split(' '))

stacks = []
cycle = 0
x = 1
crt_cycle = 0

crt = []
for i in range(0,240):
    crt.append('.')

def printCRT():
    for i in range(0,6):
        for j in range(0,40):
            print(crt[i * 40 + j],end="")
        print()

for ins in puzzleinput:
    
    if ins[0] == "noop":
        if crt_cycle % 40 == x or crt_cycle % 40 == x-1 or crt_cycle % 40 == x+1:
            crt[crt_cycle] = '#'
        cycle += 1
        crt_cycle += 1
    else:
        if crt_cycle % 40 == x or crt_cycle % 40 == x-1 or crt_cycle % 40 == x+1:
            crt[crt_cycle] = '#'
        cycle += 1
        crt_cycle += 1

        if crt_cycle % 40 == x or crt_cycle % 40 == x-1 or crt_cycle % 40 == x+1:
            crt[crt_cycle] = '#'
        cycle += 1
        crt_cycle += 1
        x += int(ins[1])

printCRT()
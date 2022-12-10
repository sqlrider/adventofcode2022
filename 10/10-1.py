# Advent of Code 2022 - Puzzle 10-1

puzzleinput = []

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip('\n')
        puzzleinput.append(line.split(' '))

#print(puzzleinput)

stacks = []
cycle = 0
x = 1
signal_strength = 0

for ins in puzzleinput:
    
    if ins[0] == "noop":
        print("No instruction")
        cycle += 1
        #print("Cycle",cycle, ", x = ",x)
        if cycle in set([20,60,100,140,180,220]):
            signal_strength += x * cycle
    else:
        print("Add ",ins[1])
        #print("Cycle",cycle, ", x = ",x)
        cycle += 1
        if cycle in set([20,60,100,140,180,220]):
            signal_strength += x * cycle
        #print("Cycle",cycle, ", x = ",x)
        cycle += 1
        if cycle in set([20,60,100,140,180,220]):
            signal_strength += x * cycle
        x += int(ins[1])

print("Signal strength: ",signal_strength)


   



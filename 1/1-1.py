# Advent of Code 2022 - Puzzle 1-1

calorielist = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        calorielist.append(line)

cals = 0
highestcals = 0

for entry in calorielist:
    if entry:
        cals = cals + int(entry)
    else:
        if cals > highestcals:
            highestcals = cals
        cals = 0
    #print('Cals: ', cals, ', Highestcals = ', highestcals)
    
print('Highest calorie count: ', highestcals)

file.close()
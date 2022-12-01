# Advent of Code 2022 - Puzzle 1-2

calorielist = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        calorielist.append(line)

calorie_totals = []

currentcals = 0

for entry in calorielist:
    if entry:
        currentcals = currentcals + int(entry)
    else:
        calorie_totals.append(currentcals)
        currentcals = 0
    #print('Cals: ', currentcals)
    
calorie_totals.sort(reverse=1)

top_3_calories_total = calorie_totals[0] + calorie_totals[1] + calorie_totals[2]

print('Top 3 calories total: ', top_3_calories_total)

file.close()
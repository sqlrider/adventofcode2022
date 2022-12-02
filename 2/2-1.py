
# Advent of Code 2022 - Puzzle 2-1

# A, X = Rock, 1 pt
# B, Y = Paper, 2 pt
# C, Z = Scissors, 3 pt
#
# Lose = 0 pt, Draw = 3 pt, Win = 6 pt

games = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        games.append(line)

score = 0


for round in games:
    if round[0] == 'A':
        if round[2] == 'X':     # Rock/Rock draw 1 + 3
            score += 4
        elif round[2] == 'Y':   # Rock/Paper win 2 + 6
            score += 8
        elif round[2] == 'Z':   # Rock/Scissors lose 3 + 0
            score += 3
    elif round[0] == 'B':
        if round[2] == 'X':     # Paper/Rock lose 1 + 0
            score += 1
        elif round[2] == 'Y':   # Paper/Paper draw 2 + 3
            score += 5
        elif round[2] == 'Z':   # Paper/Scissors win 3 + 6
            score += 9
    elif round[0] == 'C':
        if round[2] == 'X':     # Scissors/Rock win 1 + 6
            score += 7
        elif round[2] == 'Y':   # Scissors/Paper lose 2 + 0
            score += 2
        elif round[2] == 'Z':   # Scissors/Scissors draw 3 + 3
            score += 6

print('Total score: ', score)

# Advent of Code 2022 - Puzzle 2-2

# A, X = Rock, 1 pt
# B, Y = Paper, 2 pt
# C, Z = Scissors, 3 pt
#
# Lose = 0 pt, Draw = 3 pt, Win = 6 pt
#
# X = must lose
# Y = must draw
# Z = must win

games = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        games.append(line)

score = 0


for round in games:
    if round[0] == 'A':
        if round[2] == 'X':     # Must lose to rock, so Rock/Scissors = 3 + 0 = 3
            score += 3
        elif round[2] == 'Y':   # Must draw to rock, so Rock/Rock = 1 + 3 = 4
            score += 4
        elif round[2] == 'Z':   # Must win to rock, so Rock/Paper = 2 + 6 = 8
            score += 8
    elif round[0] == 'B':
        if round[2] == 'X':     # Must lose to paper, so Paper/Rock = 1 + 0 = 1
            score += 1
        elif round[2] == 'Y':   # Must draw to paper, so Paper/Paper = 2 + 3 = 5
            score += 5
        elif round[2] == 'Z':   # Must win to paper, so Paper/Scissors = 3 + 6 = 9
            score += 9
    elif round[0] == 'C':
        if round[2] == 'X':     # Must lose to scissors, so Scissors/Paper = 2 + 0 = 2
            score += 2
        elif round[2] == 'Y':   # Must draw to scissors, so Scissors/Scissors = 3 + 3 = 6
            score += 6
        elif round[2] == 'Z':   # Must win to scissors, so Scissors/Rock = 1 + 6 = 7
            score += 7

print('Total score: ', score)
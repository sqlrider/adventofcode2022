# Advent of Code 2022 - Puzzle 3-2

bags = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        bags.append(line)

priority = 0

for x in range(0,100):
    y = x * 3  # Have to do this as Python doesn't appear to support incrementors in loop syntax
    common_letter = next(iter(set(bags[y]) & set(bags[y+1]) & set(bags[y+2])))
    if common_letter >= 'a' and common_letter <= 'z':
        print(common_letter, ': ', ord(common_letter) - 96)
        priority += ord(common_letter) - 96
    elif common_letter >= 'A' and common_letter <= 'Z':
        print(common_letter, ': ', ord(common_letter) - 38)
        priority += ord(common_letter) - 38

print('Total priority: ', priority)
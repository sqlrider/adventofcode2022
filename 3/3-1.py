# Advent of Code 2022 - Puzzle 3-1

bags = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        bags.append(line)

match = 0
priority = 0

for bag in bags:
    bag1 = bag[:int(len(bag)/2)]
    bag2 = bag[int(len(bag)/2):]
    print(bag1, ' ', bag2)
    common_letter = next(iter(set(bag1) & set(bag2)))
    if common_letter >= 'a' and common_letter <= 'z':
        print(common_letter, ': ', ord(common_letter) - 96)
        priority += ord(common_letter) - 96
    elif common_letter >= 'A' and common_letter <= 'Z':
        print(common_letter, ': ', ord(common_letter) - 38)
        priority += ord(common_letter) - 38

print('Total priority: ', priority)
    
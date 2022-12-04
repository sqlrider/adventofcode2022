# Advent of Code 2022 - Puzzle 4-1

ranges = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        ranges.append(line)

overlaps = 0

for rng in ranges:
    r = rng.split(',')
    r1 = r[0].split('-')
    r2 = r[1].split('-')
    range1 = range(int(r1[0]), int(r1[1]))
    range2 = range(int(r2[0]), int(r2[1]))
    if (range1.start >= range2.start and range1.stop <= range2.stop) or (range2.start >= range1.start and range2.stop <= range1.stop):
        overlaps += 1

print('Number of overlaps: ', overlaps)


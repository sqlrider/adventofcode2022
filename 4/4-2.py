# Advent of Code 2022 - Puzzle 4-2

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
    result = range(max(range1.start,range2.start), min(range1.stop,range2.stop)+1)
    if len(list(result)) > 0:
        overlaps += 1

print('Number of overlaps: ', overlaps)


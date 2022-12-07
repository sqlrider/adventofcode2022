# Advent of Code 2022 - Puzzle 7-1

puzzleinput = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        puzzleinput.append(line)


# Use a dictionary object to map directory paths to total sizes
result = dict({"root":0})
# But also need a list representing current path as paths are traversed
current_dir = []

for line in puzzleinput:
    print(line)
    if line.startswith('$ cd'):
        if line == "$ cd /":
            print("Currently in root")
            current_dir.append("root")
        elif line == '$ cd ..':  # If traversing back up, just pop the last value from the current_dir stack
            print("Changing directory from", current_dir[-1], current_dir[-2])
            current_dir.pop()
        else:
            # On changing directories, append the new absolute path to our current_dir stack
            path = "/".join([current_dir[-1],line[5:]])
            print("Changing directory from", current_dir[-1], "to", path)
            current_dir.append(path)
            result[current_dir[-1]] = 0     # Create a 0 value dictionary entry for the current absolute path

    if line[0].isdigit():
        f = line.split(' ')
        print("Adding file named", f[1], "of size", f[0], "to", current_dir[-1], "and parent folders")
        # Loop through current and parent paths in dictionary and add filesize to *all* of the values
        for dir in current_dir:
            result[dir] += int(f[0])

# print(result)

totalsize = 0

for path, size in result.items():
    if size < 100000:
        totalsize += size

print("Total size:", totalsize)
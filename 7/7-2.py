# Advent of Code 2022 - Puzzle 7-2

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

diskspace = 70000000
total_used = result["root"]
free_space = diskspace - total_used
required_free = 30000000 - free_space
print("Disk space:", diskspace)
print("Total used:", total_used)
print("Free space:", free_space)
print("Required extra free space:", required_free)

folder_size_to_delete = 999999999   # Dummy high value

for path, size in result.items():
    if size > required_free:
        if size < folder_size_to_delete:
            folder_size_to_delete = size

print("Minimum dir size to delete:", folder_size_to_delete)

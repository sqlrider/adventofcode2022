# Advent of Code 2022 - Puzzle 12-2
from queue import PriorityQueue

puzzleinput = []

with open("input.txt", 'r') as file:
    for line in file:
        puzzleinput.append(line.strip('\n'))

height = len(puzzleinput)
width = len(puzzleinput[0])

# Define node class holding grid coords, letter, elevation and neighbours of node. Default cost to visit of 9999 and came_from as None as unvisited
class Node():
    def __init__(self, y, x, letter, elevation):
        self.y = y
        self.x = x
        self.letter = letter
        self.elevation = elevation
        self.neighbours = []
        self.cost_to_visit = 9999
        self.came_from = None

    def AddNeighbour(self, neighbour):
        self.neighbours.append(neighbour)

# Create list of nodes
nodes = []
for y in range(0, len(puzzleinput)):
    for x in range(0, len(puzzleinput[0])):
        tmp_elev = ord(puzzleinput[y][x]) - 96
        if tmp_elev == -13:
            tmp_elev = 1
        if tmp_elev == -27:
            end = (y,x) # Use later on in reconstructing path
            tmp_elev = 26
        nodes.append(Node(y, x, puzzleinput[y][x],tmp_elev))

# Add neighbours for each node
for n in nodes:
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    for dir in directions:
        # If neighbour is within bounds of grid
        if 0 <= n.y + dir[0] < height and 0 <= n.x + dir[1] < width:
            # If traversal is possible (elevation at most 1 higher)
            for ne in nodes:
                if ne.y == n.y + dir[0] and ne.x == n.x + dir[1]:
                    if ne.elevation - 1 <= n.elevation:
                        n.AddNeighbour(ne)


# Part 2
# Get list of nodes of height 'a'
start_nodes = []
shortest_path = 9999

for n in nodes:
    if n.letter == 'a':
        start_nodes.append(n)

# Loop over 'a' start nodes updating shortest_path each time if a shorter path found
for a in start_nodes:

    nodes_to_visit = PriorityQueue()

    # Get start node and add this to queue, and save node ref for path reconstruction later
    a.cost_to_visit = 0
    start = a
    nodes_to_visit.put((0,id(a),a))

    while not nodes_to_visit.empty():

        current = nodes_to_visit.get()

        if current[2].letter == 'E':
            if current[2].cost_to_visit < shortest_path:
                print("Found new shortest path, cost =", current[2].cost_to_visit)
                shortest_path = current[2].cost_to_visit
            print("Found exit, cost =", current[2].cost_to_visit)
            break

        for ne in current[2].neighbours:
            new_cost = current[2].cost_to_visit + 1
            if new_cost < ne.cost_to_visit:
                ne.cost_to_visit = new_cost
                priority = new_cost
                nodes_to_visit.put((priority, id(ne), ne))
                ne.came_from = current[2]

    # Reset node costs/came_from
    for n in nodes:
        n.cost_to_visit = 9999
        n.came_from = None

print("Shortest path:",shortest_path)

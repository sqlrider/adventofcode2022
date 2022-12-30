# Advent of Code 2022 - Puzzle 12-1
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

# Create a priority queue to hold unvisited/re-visited nodes in with priority based on cost to traverse to them
nodes_to_visit = PriorityQueue()

# Get start node and add this to queue with cost to visit and priority 0, and save reference to it, and end node, for path reconstruction later.
# Need to add id(n) - an auto-generated unique value per node - as second value otherwise the PriorityQueue's
# internal comparison mechanism breaks when multiple nodes are in queue with same priority, expected in a graph
# of uniform costs. Further prioritising is unneccessary in such cases, so use id(n) as a meaningless tiebreaker.
for n in nodes:
    if n.letter == 'S':
        nodes_to_visit.put((0,id(n),n))
        n.cost_to_visit = 0
        start_node = n
    if n.letter == 'E':
        end_node = n


while not nodes_to_visit.empty():

    current = nodes_to_visit.get()

    # Exit search early if found exit
    if current[2].letter == 'E':
        print("Found exit, cost =", current[2].cost_to_visit)
        break

    for ne in current[2].neighbours:
        new_cost = current[2].cost_to_visit + 1    # Edge weights are always 1 for this puzzle
        # Check if cost just calculated to get to neighbour is lower than the stored cost for it
        if new_cost < ne.cost_to_visit: 
            # Assign new cost to it, then add it to the priority queue with that new cost as priority
            ne.cost_to_visit = new_cost
            priority = new_cost
            nodes_to_visit.put((priority, id(ne), ne))
            ne.came_from = current[2]  # Update neighbour's came_from node reference to say we visited it from current node
            #print("Found neighbour",ne.letter,"at",ne.y,",",ne.x,", setting cost to",new_cost)

# Reconstruct path from 'end' node to 'start'.
# Loop over came_from values from end node to to backtrack to 'start', appending y,x coords to path as we go
current = end_node
path = []
path.append(current)

while current != start_node:
    current = current.came_from
    path.append((current.y, current.x))

for i in range(0, height):
    for j in range(0, width):
        if (i,j) in path:
            print("\033[31m*\033[0m",end='')
        else:
            print(puzzleinput[i][j],end='')
    print()


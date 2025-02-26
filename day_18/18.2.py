import heapq
import numpy as np

filename = 'input.txt'
data = np.loadtxt(filename, dtype=list, delimiter=',')

new_data = []
for row in data:
    new_data.append([])
    for item in row:
        new_data[-1].append(int(item))

data = np.array(new_data)

if filename == 'test.txt':
    m = 7
    n = 7
else:
    m=71
    n=71

def dijkstra(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    distances = { (i, j): float('inf') for i in range(rows) for j in range(cols) }
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == goal:
            break

        neighbors = get_neighbors(current_node, rows, cols)
        for neighbor in neighbors:
            if grid[neighbor[0]][neighbor[1]] == '#':
                continue
            distance = current_distance + 1
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[goal]

def get_neighbors(node, rows, cols):
    i, j = node
    neighbors = []
    if i > 0:
        neighbors.append((i-1, j))
    if i < rows - 1:
        neighbors.append((i+1, j))
    if j > 0:
        neighbors.append((i, j-1))
    if j < cols - 1:
        neighbors.append((i, j+1))
    return neighbors


start = (0, 0)
goal = (m-1, n-1)

for i in range(1,len(data)+1):

    print('i',i)
    grid  = [['.' for j in range(n)] for i in range(m)]

    for row in data[:i]:
        grid[row[0]][row[1]] = '#'

    shortest_path_distance = dijkstra(grid, start, goal)
    print('Shortest path distance:', shortest_path_distance)
    if shortest_path_distance == float('inf'):
        print('last coordinate:', data[i-1])
        break
import heapq
from collections import Counter

grid = []
with open('input.txt','r') as file:
    for line in file:
        grid.append(list(line.strip()))

m = len(grid)
n = len(grid[0])

positions = set()

directions = [(0,1),(1,0),(0,-1),(-1,0)]

for i in range(m):
    for j in range(n):

        if grid[i][j] == 'S':
            start = (i,j)

        if grid[i][j] == 'E':
            end = (i,j)

        if grid[i][j] == '#':
            positions.add((i,j))


print(len(positions))

def dijkstra(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    distances = { (i, j): float('inf') for i in range(rows) for j in range(cols) }
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()
    previous_nodes = {start: None}

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
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    path = set()
    current = goal
    while current is not None:
        path.add(current)
        current = previous_nodes.get(current)

    return distances[goal], path

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


min_distance = float('inf')
total = 0
cnt = 0
pos_len = len(positions)

og_distance, og_path = dijkstra(grid,start,end)
print(og_distance)
all_saves = []

for item in positions:
    cnt += 1
    print(cnt/pos_len)
    if cnt % 1000 == 0:
        for i in range(100):
            print('TOTAL', total)
 
    new_grid = [row.copy() for row in grid]
    new_grid[item[0]][item[1]] = 'O'
    new_distance, path = dijkstra(new_grid,start,end)
    if (item[0],item[1]) in path:
        if og_distance - new_distance >= 100:

            total += 1
            all_saves.append(og_distance-new_distance)

print('og_distance', og_distance)
print('total', total)
print('max save', max(all_saves))

d = Counter(all_saves)
print(d)




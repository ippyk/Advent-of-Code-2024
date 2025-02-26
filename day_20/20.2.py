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



def dijkstra(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    distances = {}

    for i in range(m):
        for j in range(n):
            if not grid[i][j] == '#':
                distances[(i,j)] = float('inf')

    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()
    previous_nodes = {start: None}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        visited.add(current_node)
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

    return distances, path

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

end_distances, end_path = dijkstra(grid,end,start)
start_distances, start_path = dijkstra(grid,start,end)
all_saves = []


seen = {}
directions = [(0,1),(1,0),(0,-1),(-1,0)]

target = 20

for  i in range(m):
    print(i)
    for j in range(n):

        for p in range(m):
            for q in range(n):

                if (not i == p) or (not j == q):

                    if (not grid[i][j] == '#') and (not grid[p][q] == '#'):


                        distance = abs(i-p) + abs(j-q)

                        if distance <= target:

                            seen[((i,j),(p,q))] = abs(i-p) + abs(j-q)


amounts = []
og_distance = start_distances[end]
total = 0

print('OG DISTANCE', og_distance)

seen_len = len(seen)
seen_cnt = 0

for item in seen:

    seen_cnt += 1
    print(seen_cnt/seen_len)

    total_distance = start_distances[item[0]]+end_distances[item[1]]+seen[item]

    if total_distance < og_distance:

        if og_distance - total_distance >= 100:

            amounts.append(og_distance - total_distance)
            total += 1
        
d = Counter(amounts)
print(d)
print('total', total)







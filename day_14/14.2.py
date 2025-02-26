import re
import matplotlib.pyplot as plt
import numpy as np

with open('input.txt', 'r') as file:
    text = file.read()

pattern = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')
matches = pattern.findall(text)
numbers = [list(map(int, match)) for match in matches]

def generate_heatmap(grid, iter):
    data = np.array([[1 if cell == '.' else 0 for cell in row] for row in grid])
    
    plt.imshow(data, cmap='gray', interpolation='nearest')
    plt.axis('off') 
    plt.savefig(f'images/{iter}.png', bbox_inches='tight', pad_inches=0)
    plt.close()

m = 103
n = 101

grid = [['.' for _ in range(n)] for _ in range(m)]

for item in numbers:
    if grid[item[1]][item[0]] == '.':
        grid[item[1]][item[0]] = '1'
    else:
        grid[item[1]][item[0]] = str(int(grid[item[1]][item[0]]) + 1)

def check_single(grid, i, j):


    up = False
    if i-1 >= 0:
        if not grid[i-1][j] == '.':
            up = True

    left = False
    if j-1 >= 0:
        if not grid[i][j-1] == '.':
            left = True

    down = False
    if i+1 <= m-1:
        if not grid[i+1][j] == '.':
            down = True

    right = False
    if j+1 <= n-1:
        if not grid[i][j+1] == '.':
            right = True

    return up or left or down or right

iters = -1
while iters < 10_000:
    print('iters1',iters)
    iters += 1
    final_grid = [['.' for _ in range(n)] for _ in range(m)]
    for item in numbers:


        x = item[0]
        y = item[1]
        v1 = item[2]
        v2 = item[3]

        final_x = (x + iters*v1) % n
        final_y = (y + iters*v2) % m

        if final_grid[final_y][final_x] == '.':
            final_grid[final_y][final_x] = '1'
        else:
            final_grid[final_y][final_x] = str(int(final_grid[final_y][final_x]) + 1)

    generate_heatmap(final_grid, iters)


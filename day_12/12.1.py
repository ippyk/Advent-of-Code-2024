with open('input.txt', 'r') as file:
        grid = []
        for line in file:
            row = list(line.strip())
            grid.append(row)

m = len(grid)
n = len(grid[0])

def recur(letter, i, j, grid):

    area = 0
    perimeter = 0

    if grid[i][j] == letter:
        grid[i][j] += '-'
        area += 1
      
    if i-1 >= 0 :
        if grid[i-1][j] == letter:
            new_area, new_perimeter = recur(letter, i-1, j, grid)
            area += new_area
            perimeter += new_perimeter
        elif not grid[i-1][j] == letter + '-':
            perimeter += 1
    else:
        perimeter += 1

    if j-1 >= 0:
        if grid[i][j-1] == letter:
            new_area, new_perimeter = recur(letter, i, j-1, grid)
            area += new_area
            perimeter += new_perimeter
        elif not grid[i][j-1] ==  letter + '-':
            perimeter += 1
    else:
        perimeter += 1

    if i+1 <= m-1:
        if grid[i+1][j] == letter:
            new_area, new_perimeter = recur(letter, i+1, j, grid)
            area += new_area
            perimeter += new_perimeter
        elif not grid[i+1][j] == letter + '-':
            perimeter += 1
    else:
        perimeter += 1

    if j+1 <= n-1:
        if grid[i][j+1] == letter:
            new_area, new_perimeter = recur(letter, i, j+1, grid)
            area += new_area
            perimeter += new_perimeter
        elif not grid[i][j+1] == letter + '-':
            perimeter += 1
    else:
        perimeter += 1

    return area, perimeter


seen = {}

grid_copy = [row.copy() for row in grid]
cnt = 0

for i in range(m):
    for j in range(n):

        if (not grid_copy[i][j][-1] == '-'):
            cnt += 1
            letter = grid_copy[i][j]
            area, perimeter = recur(letter, i, j, grid_copy)
            seen[cnt] = (area, perimeter)

total = 0

for item in seen:

    total += seen[item][0] * seen[item][1]

print(total)



    


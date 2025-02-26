with open('input.txt', 'r') as file:
        grid = []
        for line in file:
            row = list(line.strip())
            grid.append(row)

m = len(grid)
n = len(grid[0])

def recur(letter, i, j, grid, sides):

    area = 0
    perimeter = 0

    if grid[i][j] == letter:
        grid[i][j] += '-'
        area += 1
    else:
        return 0, 0
      
    if i-1 >= 0 :
        if grid[i-1][j] == letter:
            new_area, new_perimeter = recur(letter, i-1, j, grid, sides)
            area += new_area
            perimeter += new_perimeter
        elif not grid[i-1][j] == letter + '-':
            perimeter += 1
            sides[(i,'up')] = sides.get((i,'up'), []) + [(i,j)]
    else:
        perimeter += 1
        sides[(i,'up')] = sides.get((i,'up'), []) + [(i,j)]

    if j-1 >= 0:
        if grid[i][j-1] == letter:
            new_area, new_perimeter = recur(letter, i, j-1, grid, sides)
            area += new_area
            perimeter += new_perimeter
        elif not grid[i][j-1] ==  letter + '-':
            perimeter += 1
            sides[(j,'left')] = sides.get((j,'left'), []) + [(i,j)]
    else:
        perimeter += 1
        sides[(j,'left')] = sides.get((j,'left'), []) + [(i,j)]

    if i+1 <= m-1:
        if grid[i+1][j] == letter:
            new_area, new_perimeter = recur(letter, i+1, j, grid, sides)
            area += new_area
            perimeter += new_perimeter
        elif not grid[i+1][j] == letter + '-':
            perimeter += 1
            sides[(i,'down')] = sides.get((i,'down'), []) + [(i,j)]
    else:
        perimeter += 1
        sides[(i,'down')] = sides.get((i,'down'), []) + [(i,j)]

    if j+1 <= n-1:
        if grid[i][j+1] == letter:
            new_area, new_perimeter = recur(letter, i, j+1, grid, sides)
            area += new_area
            perimeter += new_perimeter
        elif not grid[i][j+1] == letter + '-':
            perimeter += 1
            sides[(j,'right')] = sides.get((j,'right'), []) + [(i,j)]
    else:
        perimeter += 1
        sides[(j,'right')] = sides.get((j,'right'), []) + [(i,j)]

    return area, perimeter


def count_sides(sides):

    sides_cnt = 0

    for item in sides:
        cnt = 0 

        if len(sides[item]) == 1:
            sides_cnt += 1
            continue


        if item[1] == 'up' or item[1] == 'down':


            sides[item].sort(key = lambda x: x[1])
            cnt = 1

            for i in range(1,len(sides[item])):
                if sides[item][i][1] - sides[item][i-1][1] > 1:
                    cnt += 1

        else:

            sides[item].sort(key = lambda x: x[0])
            cnt = 1

            for i in range(1,len(sides[item])):
                if sides[item][i][0] - sides[item][i-1][0] > 1:
                    cnt += 1

        sides_cnt += cnt

    return sides_cnt



seen = {}

grid_copy = [row.copy() for row in grid]
cnt = 0

for i in range(m):
    for j in range(n):

        if (not grid_copy[i][j][-1] == '-'):
            sides = {}
            cnt += 1
            letter = grid_copy[i][j]
            area, perimeter = recur(letter, i, j, grid_copy, sides)
            sides_cnt = count_sides(sides)
            seen[cnt] = (area, sides_cnt)

total = 0

for item in seen:

    total += seen[item][0] * seen[item][1]

print(total)



    


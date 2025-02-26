with open('input.txt', 'r') as file:
        og_grid = []
        for line in file:
            row = list(line.strip())
            og_grid.append(row)


# for row in grid:
#     print(row)

print('BREAK')

m = len(og_grid)
n = len(og_grid[0])
print('m,n',m,n)

found = False
og_direction = None

for i in range(m):
    for j in range(n):
        if og_grid[i][j] == '^':
            start = (i,j)
            found = True
            og_direction = 'up'
            break
        elif og_grid[i][j] == '>':
            start = (i,j)
            found = True
            og_direction = 'right'
            break
        elif og_grid[i][j] == 'v':
            start = (i,j)
            found = True
            og_direction = 'down'
            break
        elif og_grid[i][j] == '<':
            start = (i,j)
            found = True
            og_direction = 'left'
            break

    if found:
         break
    
cnt2 = 0

# for p in range(m):
#     for q in range(n):
#         print(p,q)

#         grid = [row.copy() for row in og_grid]
#         if grid[p][q] == '.':
#             grid[p][q] = '#'
#         else:
#             continue

#         cnt = 0
#         seen = []
#         i,j = start[0], start[1]
#         direction = og_direction

#         if p == i and q == j:
#             continue

cnt = 0
path = []
i,j = start[0], start[1]
direction = og_direction
grid = [row.copy() for row in og_grid]

        
while (i >= 0) and (i <= m-1) and (j >= 0) and (j <= n-1):

    if not grid[i][j] == '0':
        grid[i][j] = '0'
        cnt += 1

    if direction == 'up':
        if i-1>=0 and grid[i-1][j] == '#':
            direction = 'right'

            if j+1<=n-1 and grid[i][j+1] == '#':
                continue

            j += 1
        else:

            if i-1>=0:
                path.append((i-1,j))

            i -= 1
                    
        continue

    if direction == 'right':
        if j+1<=n-1 and grid[i][j+1] == '#':
            direction = 'down'

            if i+1<=m-1 and grid[i+1][j] == '#':
                continue
            i += 1
        else:

            if j+1<=n-1:
                path.append((i,j+1))

            j += 1

        continue

    if direction == 'down':
        if i+1<=m-1 and grid[i+1][j] == '#':
            direction = 'left'

            if j-1>=0 and grid[i][j-1] == '#':
                continue

            j -= 1
        else:

            if i+1<=m-1:
                path.append((i+1,j))

            i += 1

        continue

    if direction == 'left':
        if j-1>=0 and grid[i][j-1] == '#':
            direction = 'up'


            if i-1>=0 and grid[i-1][j] == '#':
                continue

            i -= 1
        else:

            if j-1>=0:
                path.append((i,j-1))

            j -= 1

        continue

# for row in grid:
#     print(row)

print('PATH LEN', len(path))
path = set(path)

path = []
for p in range(m):
    for q in range(n):

        if grid[p][q] == start:
            continue
        else:
            path.append((p,q))


print('hey')
progress = 0
path_len = len(path)



for item in path:

    print((progress+1) /path_len)
    progress += 1

    p, q = item[0], item[1]
    grid = [row.copy() for row in og_grid]
    if grid[p][q] == '.':
        grid[p][q] = '#'
    else:
        continue

    seen = set()
    i,j = start[0], start[1]
    direction = og_direction

    if p == i and q == j:
        continue


    while (i >= 0) and (i <= m-1) and (j >= 0) and (j <= n-1):

        if (i,j,direction) in seen:
            cnt2 += 1
            break
        else:
            seen.add((i,j,direction))


        if direction == 'up':
            if i-1>=0 and grid[i-1][j] == '#':
                direction = 'right'

                if j+1<=n-1 and grid[i][j+1] == '#':
                    continue
                else:
                    j += 1
            else:

                i -= 1
                        
            continue

        if direction == 'right':
            if j+1<=n-1 and grid[i][j+1] == '#':
                direction = 'down'

                if i+1<=m-1 and grid[i+1][j] == '#':    
                    continue
                else:
                    i += 1
            else:

                j += 1

            continue

        if direction == 'down':
            if i+1<=m-1 and grid[i+1][j] == '#':
                direction = 'left'

                if j-1>=0 and grid[i][j-1] == '#':
                    continue
                else:
                    j -= 1
            else:

                i += 1

            continue

        if direction == 'left':
            if j-1>=0 and grid[i][j-1] == '#':
                direction = 'up'

                if i-1>=0 and grid[i-1][j] == '#':
                    continue
                else:
                    i -= 1

            else:

                j -= 1

            continue

print(cnt2)



    


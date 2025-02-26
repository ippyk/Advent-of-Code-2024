with open('input.txt', 'r') as file:
        grid = []
        s = ''
        grid_finished = False
        for line in file:

            if line == '\n':
                grid_finished = True
                continue

            if not grid_finished:
                row = list(line.strip())
                grid.append(row)
            else:
                s += line.strip()

m = len(grid)
n = len(grid[0])

start_found = False
for i in range(m):
    for j in range(n):
        if grid[i][j] == '@':
            start = (i,j)
            start_found = True
            break
    if start_found:
        break

vector_map = {'^': (-1,0), 'v': (1,0), '<': (0,-1), '>': (0,1)}

grid2 = [row.copy() for row in grid]
pos = start

def mover(i,j,dir,pos):

    dir_vec = vector_map[dir]
    cnt = 1

    while grid2[i+cnt*dir_vec[0]][j+cnt*dir_vec[1]] == 'O':
        
        cnt += 1

    if grid2[i+cnt*dir_vec[0]][j+cnt*dir_vec[1]] == '#':
        pass
    elif grid2[i+cnt*dir_vec[0]][j+cnt*dir_vec[1]] == '.':
        grid2[i+cnt*dir_vec[0]][j+cnt*dir_vec[1]] = 'O'
        grid2[i+dir_vec[0]][j+dir_vec[1]] = '@'
        grid2[i][j] = '.'
        pos = (pos[0]+dir_vec[0],pos[1]+dir_vec[1])
    else:
        print(f'what is going on? {grid[i+cnt*dir_vec[0]][j+cnt*dir_vec[1]]}')

    return pos


for dir in s:

    dir_vec = vector_map[dir]

    if grid2[pos[0]+dir_vec[0]][pos[1]+dir_vec[1]] == 'O':
        pos = mover(pos[0], pos[1], dir, pos)
    elif grid2[pos[0]+dir_vec[0]][pos[1]+dir_vec[1]] == '.':
        grid2[pos[0]][pos[1]] = '.'
        grid2[pos[0]+dir_vec[0]][pos[1]+dir_vec[1]] = '@'
        pos = (pos[0]+dir_vec[0],pos[1]+dir_vec[1])
    else:
        continue
    
total = 0
for i in range(m):
    for j in range(n):

        if grid2[i][j] == 'O':
            total += 100*i+j

print(total)
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

new_grid = []

for row in grid:
    new_row = []
    for item in row:
        if item == '#':
            new_row.append('#')
            new_row.append('#')
        elif item == 'O':
            new_row.append('[')
            new_row.append(']')
        elif item == '.':
            new_row.append('.')
            new_row.append('.')
        elif item == '@':
            new_row.append('@')
            new_row.append('.')
    new_grid.append(new_row)

grid = [row.copy() for row in new_grid]
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

def structure(i,j,dir):

    seen = set()
    blocker = [False]
    dir_vec = vector_map[dir]
    recur(i,j,dir,seen,blocker)

    if not blocker[0]:
        for item in seen:
            grid2[item[0]][item[1]] = '.'

        for item in seen:
            grid2[item[0]+dir_vec[0]][item[1]] = item[2]

    return blocker[0]

def recur(i,j,dir,seen,blocker):

    dir_vec = vector_map[dir]

    if grid2[i+dir_vec[0]][j] == '#':
        blocker[0]  = True
        return

    if grid2[i][j] == '[' or grid2[i][j] == ']':
        if (i,j,grid2[i][j]) not in seen:
            seen.add((i,j,grid2[i][j]))
        else:
            return

    if grid2[i][j-1] == '[':
        recur(i,j-1,dir,seen,blocker)

    if grid2[i][j+1] == ']':
        recur(i,j+1,dir,seen,blocker),

    if grid2[i+dir_vec[0]][j] == '[' or grid2[i+dir_vec[0]][j] == ']':
        recur(i+dir_vec[0],j,dir,seen,blocker)


def mover(i,j,dir,pos):

    dir_vec = vector_map[dir]
    cnt = 1

    while grid2[i+cnt*dir_vec[0]][j+cnt*dir_vec[1]] == ']' or grid2[i+cnt*dir_vec[0]][j+cnt*dir_vec[1]] == '[':
            
            cnt += 1

    if grid2[i+cnt*dir_vec[0]][j+cnt*dir_vec[1]] == '#':
        pass
    elif grid2[i+cnt*dir_vec[0]][j+cnt*dir_vec[1]] == '.':

        if dir == '>':
            begin = True
            for k in range(j+2*dir_vec[1],j+(cnt+1)*dir_vec[1]):
                if begin:
                    grid2[i][k] = '['
                    begin = False
                else:
                    grid2[i][k] = ']'
                    begin = True

            grid2[i+dir_vec[0]][j+dir_vec[1]] = '@'
            grid2[i][j] = '.'
            pos = (pos[0]+dir_vec[0],pos[1]+dir_vec[1])

        elif dir == '<':
            begin = True
            for k in range(j+2*dir_vec[1],j+(cnt+1)*dir_vec[1],-1):
                if begin:
                    grid2[i][k] = ']'
                    begin = False
                else:
                    grid2[i][k] = '['
                    begin = True

            grid2[i+dir_vec[0]][j+dir_vec[1]] = '@'
            grid2[i][j] = '.'
            pos = (pos[0]+dir_vec[0],pos[1]+dir_vec[1])

        elif dir == '^' or dir == 'v':

            if grid2[i+dir_vec[0]][j+dir_vec[1]] == ']' or grid2[i+dir_vec[0]][j+dir_vec[1]] == '[':
                blocked_val = structure(i,j,dir)

                if not blocked_val:
                    grid2[i+dir_vec[0]][j+dir_vec[1]] = '@'
                    grid2[i][j] = '.'
                    pos = (pos[0]+dir_vec[0],pos[1]+dir_vec[1])

            else:

                grid2[i+dir_vec[0]][j+dir_vec[1]] = '@'
                grid2[i][j] = '.'
                pos = (pos[0]+dir_vec[0],pos[1]+dir_vec[1])

        else:
            pass

    else:
        pass


    return pos


for dir in s:

    dir_vec = vector_map[dir]

    if grid2[pos[0]+dir_vec[0]][pos[1]+dir_vec[1]] == '[' or grid2[pos[0]+dir_vec[0]][pos[1]+dir_vec[1]] == ']':
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

        if grid2[i][j] == '[':
            total += 100*i+j

print(total)
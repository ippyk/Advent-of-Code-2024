import sys
sys.setrecursionlimit(20_000)
 
grid = []
with open('input.txt','r') as file:
    for line in file:
        grid.append(list(line.strip()))
 
m = len(grid)
n = len(grid[0])
 
for i in range(m):
    for j in range(n):
        if grid[i][j] == 'S':
            start = (i,j)
        elif grid[i][j] == 'E':
            end = (i,j)

dirs = {0:(0,1),1:(-1,0),2:(0,-1),3:(1,0)}
 
seen = set()
scores = set()
cnt = [0]
max_path = [0]
min_i = [float('inf'),float('inf')]
grid_copy = [row.copy() for row in grid]
min_scores = [float('inf')]
 
grid_vals = []
for i in range(m):
    grid_vals.append([])
    for j in range(n):
        grid_vals[i].append([])
        for d in range(4):
            grid_vals[i][j].append(float('inf'))
 
with open('min_val.txt', 'w') as file:
    file.write('no scores yet')

paths = []
 
def recur(i,j,direction,score,seen,path):

    if (i,j) not in path:
        path.add((i,j))

    cnt[0] += 1
    if cnt[0] % 20_000 == 0:
        print(cnt[0])
        with open('explored.txt','w') as file:
            for row in grid_copy:
                #print(row)
                file.write(''.join(row)+'\n')
 
        with open('min_val.txt','a') as file:
            if scores:
                if min(scores) < min_scores[0]:
                    min_scores[0] = min(scores)
                    file.write(str(min_scores[0])+'\n')
 
    if (i,j,direction) in seen:
        if score > grid_vals[i][j][direction]:
            return
   
    grid_vals[i][j][direction] = min(score,grid_vals[i][j][direction])
 
    if grid_copy[i][j] == '.':
        grid_copy[i][j] = '0'

    seen.add((i,j,direction))
 
    if grid[i][j] == 'E':
        
        if scores:
            best_score_so_far = min(scores)
            if score < best_score_so_far:
                paths.clear()
                paths.append(path)
            elif score == best_score_so_far:
                paths.append(path)
            else:
                pass
        else:
            paths.append(path)

        scores.add(score)

        return
 
    for dir in dirs:
        dir_vec = dirs[dir]
        if (not grid[i+dir_vec[0]][j+dir_vec[1]] == '#'):
 
            new_score  = score
            if dir==direction:
                pass
            elif dir == (direction-1)%4 or dir == (direction+1)%4:
                new_score += 1000
 
            else:
                new_score += 2*1000
 
            new_score += 1
            path_copy = path.copy()
            recur(i+dir_vec[0],j+dir_vec[1],dir,new_score,seen,path_copy)
 
 
recur(start[0],start[1],0,0,seen,set())

with open('explored.txt','w') as file:
    for row in grid_copy:
        file.write(''.join(row)+'\n')
 
 
print('len paths', len(paths))
union = set.union(*paths)
print('len union',len(union))
print('best score', min(scores))
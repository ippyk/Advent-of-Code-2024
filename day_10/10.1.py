with open('input.txt', 'r') as file:
        grid = []
        for line in file:
            row = list(line.strip())
            grid.append(row)

m = len(grid)
n = len(grid[0])
total_cnt = [0]

def recur(i,j,l,grid):

    if grid[i][j] == '9':
        grid[i][j] = '-1'

    if not l:
        total_cnt[0] += 1
        return
     
    
    if i-1 >= 0 and grid[i-1][j] == l[0]:
        l_copy = l.copy()
        l_copy.pop(0)
        val1 = recur(i-1,j,l_copy,grid)
    else:
        val1 = None
    
    if j-1 >= 0 and grid[i][j-1] == l[0]:
        l_copy = l.copy()
        l_copy.pop(0)
        val2 = recur(i,j-1,l_copy,grid)
    else:
        val2 = None
    
    if i+1 <= m-1 and grid[i+1][j] == l[0]:
        l_copy = l.copy()
        l_copy.pop(0)
        val3 = recur(i+1,j,l_copy,grid)
    else:
        val3 = None
    
    if j+1 <= n-1 and grid[i][j+1] == l[0]:
        l_copy = l.copy()
        l_copy.pop(0)
        val4 = recur(i,j+1,l_copy,grid)
    else:
        val4 = None

    return val1, val2, val3, val4

l = [str(num) for num in range(1,10)]

for i in range(m):
    for j in range(n):
        
        if grid[i][j] == '0':

            grid_copy = [row.copy() for row in grid]

            recur(i,j,l.copy(), grid_copy)

print(total_cnt[0])




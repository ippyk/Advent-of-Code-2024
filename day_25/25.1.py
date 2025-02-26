def read_grids_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    grids = []
    current_grid = []

    for line in lines:
        stripped_line = line.strip()
        if stripped_line == '':
            if current_grid:
                grids.append(current_grid)
                current_grid = []
        else:
            current_grid.append(list(stripped_line))
    
    if current_grid:
        grids.append(current_grid)

    return grids

file_path = 'input.txt'
grids = read_grids_from_file(file_path)

locks = set()
keys = set()

for grid in grids:

    if grid[0][0] == '#':
        vals = []

        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j] == '.':
                    vals.append(i-1)
                    break

        locks.add(tuple(vals))

    else:
        vals = []

        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j] == '#':
                    vals.append((len(grid)-1)-i)
                    break

        keys.add(tuple(vals))

n = len(grid[0])

total = 0

for lock in locks:

    for key in keys:

        fits = True
        for i in range(n):
            if lock[i]+key[i] > 5:
                fits = False

        if fits:
            total += 1

print('total', total)
        
    
        
            


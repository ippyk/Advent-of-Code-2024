import re

with open('input.txt', 'r') as file:
    text = file.read()

pattern = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')
matches = pattern.findall(text)
numbers = [list(map(int, match)) for match in matches]

iters = 100
m = 103
n = 101

grid = [['.' for _ in range(n)] for _ in range(m)]

for item in numbers:
    if grid[item[1]][item[0]] == '.':
        grid[item[1]][item[0]] = '1'
    else:
        grid[item[1]][item[0]] = str(int(grid[item[1]][item[0]]) + 1)

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

middle_m = m//2
middle_n = n//2

first_quater_cnt = 0
for i in range(middle_m):
    for j in range(middle_n):
        if not final_grid[i][j] == '.':
            first_quater_cnt += int(final_grid[i][j])

second_quater_cnt = 0
for i in range(middle_m):
    for j in range(middle_n+1,n):
        if not final_grid[i][j] == '.':
            second_quater_cnt += int(final_grid[i][j])

third_quater_cnt = 0
for i in range(middle_m+1,m):
    for j in range(middle_n):
        if not final_grid[i][j] == '.':
            third_quater_cnt += int(final_grid[i][j])

fourth_quater_cnt = 0
for i in range(middle_m+1,m):
    for j in range(middle_n+1,n):
        if not final_grid[i][j] == '.':
            fourth_quater_cnt += int(final_grid[i][j])

total = first_quater_cnt*second_quater_cnt*third_quater_cnt*fourth_quater_cnt
print(total)








with open('input.txt', 'r') as file:
        grid = []
        for line in file:
            row = list(line.strip())
            grid.append(row)


m = len(grid)
n = len(grid[0])

d = {}

for i in range(m):
    for j in range(n):
         
         if grid[i][j] == '.':
             continue
         else:
                if grid[i][j] not in d:
                    d[grid[i][j]] = []
                d[grid[i][j]].append((i,j))

antinodes = set()

for char in d:

    char_len = len(d[char])
    if char_len == 1:
        continue

    for p in range(char_len-1):
        for q in range(p+1,char_len):
            diff = (d[char][p][0] - d[char][q][0], d[char][p][1] - d[char][q][1])

            cnt1 = 1
            cnt2 = 1

            while 0 <= d[char][p][0]+cnt1*diff[0] <= m-1 and 0 <= d[char][p][1]+cnt1*diff[1] <= n-1:

                antinodes.add((d[char][p][0]+cnt1*diff[0], d[char][p][1]+cnt1*diff[1]))
                cnt1 += 1

            while 0 <= d[char][q][0]-cnt2*diff[0] <= m-1 and 0 <= d[char][q][1]-cnt2*diff[1] <= n-1:

                antinodes.add((d[char][q][0]-cnt2*diff[0], d[char][q][1]-cnt2*diff[1]))
                cnt2 += 1


grid_copy = [row.copy() for row in grid]
cnt = 0

for item in antinodes:
    if grid_copy[item[0]][item[1]] == '.':
        grid_copy[item[0]][item[1]] = '#'
        cnt += 1

for char in d:
    cnt += len(d[char])

print(cnt)
            



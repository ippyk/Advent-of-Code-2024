with open('input.txt', 'r') as file:
        numbers = []
        for line in file:
            row = list(line.strip())
            numbers.append(row)

m = len(numbers)
n = len(numbers[0])

def checker(i,j):

    cnt = 0

    # forward right
    if j+3<=n-1:
         if numbers[i][j] +numbers[i][j+1] + numbers[i][j+2] + numbers[i][j+3] == 'XMAS':
             cnt += 1

    # backward right
    if j+3<=n-1:
         if numbers[i][j] +numbers[i][j+1] + numbers[i][j+2] + numbers[i][j+3] == 'SAMX':
             cnt += 1

    # forward down
    if i+3<=m-1:
         if numbers[i][j] +numbers[i+1][j] + numbers[i+2][j] + numbers[i+3][j] == 'XMAS':
             cnt += 1

    # backward down
    if i+3<=m-1:
         if numbers[i][j] +numbers[i+1][j] + numbers[i+2][j] + numbers[i+3][j] == 'SAMX':
             cnt += 1

    # forward right down
    if i+3<=m-1 and j+3<=n-1:
         if numbers[i][j] +numbers[i+1][j+1] + numbers[i+2][j+2] + numbers[i+3][j+3] == 'XMAS':
             cnt += 1

    # backward right down
    if i+3<=m-1 and j+3<=n-1:
         if numbers[i][j] +numbers[i+1][j+1] + numbers[i+2][j+2] + numbers[i+3][j+3] == 'SAMX':
             cnt += 1

    # forward left down
    if i+3<=m-1 and j-3>=0:
         if numbers[i][j] +numbers[i+1][j-1] + numbers[i+2][j-2] + numbers[i+3][j-3] == 'XMAS':
             cnt += 1
      
    # backward left down
    if i+3<=m-1 and j-3>=0:
         if numbers[i][j] +numbers[i+1][j-1] + numbers[i+2][j-2] + numbers[i+3][j-3] == 'SAMX':
             cnt += 1
      

    return cnt

total = 0

for i in range(n):
     for j in range(m):
          
        total += checker(i,j)

print(total)
          


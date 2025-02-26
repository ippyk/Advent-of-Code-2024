with open('input.txt', 'r') as file:
        numbers = []
        for line in file:
            row = list(line.strip())
            numbers.append(row)

m = len(numbers)
n = len(numbers[0])

def checker(i,j):

    cnt = 0

    if i+2<=m-1 and j+2<=n-1:
         if (numbers[i][j]=='M' and numbers[i][j+2]=='M' and numbers[i+1][j+1]=='A' 
             and numbers[i+2][j]=='S' and numbers[i+2][j+2]=='S'):
             return 1
         
         if (numbers[i][j]=='S' and numbers[i][j+2]=='M' and numbers[i+1][j+1]=='A' 
             and numbers[i+2][j]=='S' and numbers[i+2][j+2]=='M'):
             return 1
         
         if (numbers[i][j]=='M' and numbers[i][j+2]=='S' and numbers[i+1][j+1]=='A' 
             and numbers[i+2][j]=='M' and numbers[i+2][j+2]=='S'):
             return 1
         
         if (numbers[i][j]=='S' and numbers[i][j+2]=='S' and numbers[i+1][j+1]=='A' 
             and numbers[i+2][j]=='M' and numbers[i+2][j+2]=='M'):
             return 1
         

    return cnt

total = 0

for i in range(n):
     for j in range(m):
          
        total += checker(i,j)

print(total)
          


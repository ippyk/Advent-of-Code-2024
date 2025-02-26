with open('input.txt', 'r') as file:
        numbers = []
        for line in file:
            row = list(map(float, line.split()))
            numbers.append(row)


errors = 0


def checker(a,b,increasing,row):

    if increasing:
                
        if row[b] <= row[a]:
            return False
                
    else:
                
        if row[b] >= row[a]:
            return False
                
    if abs(row[b] - row[a]) > 3:
        return False
        
    return True


def row_checker(row):

    n = len(row)

    if n <= 1:
        return True 
    
    if row[0] < row[1]:
        increasing = True
    else:
        increasing = False
    
    cnt = 1

    while cnt < n:
        
        val = checker(cnt-1,cnt,increasing,row)
        if not val:
            return False
                
        cnt += 1
        
    return True

pos_cnt = 0
neg_cnt = 0
l = []

for row in numbers:

    if len(row) <= 2:
        if row_checker(row):
            pos_cnt += 1
            l.append(1)
        else:
            l.append(0)
        continue

    if row_checker(row):
        pos_cnt += 1
        l.append(1)
        continue

    safe=False

    for i in range(len(row)):
        new_row = row.copy()
        new_row.pop(i)

        if row_checker(new_row):
            pos_cnt += 1
            l.append(1)
            safe=True
            break

    if not safe:
        l.append(0)

print("Positive: ", pos_cnt)
            

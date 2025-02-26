with open('input.txt', 'r') as file:
        numbers = []
        d = {}
        cnt = 0
        for line in file:

            if '|' in line:
                  num1 = ''
                  num2 = ''
                  bool1 = True
                  for i in range(len(line)):
    
                        if line[i] == '|':
                              bool1 = False
                              continue
                        
                        if bool1:
                              num1 += line[i]
                        else:
                            num2 += line[i]

                  if int(num1) in d:
                    d[int(num1)].append(int(num2))     
                  else:
                    d[int(num1)] = [int(num2)] 
            elif not line == '\n':
                    row = line.strip().split(',')
                    numbers.append([int(item) for item in row])
                


l = []

for row in numbers:

    seen = set()
    i = 0
    redos = 0
     
    while i < len(row):

        wrong_value = None

        if row[i] in d:
            for item in d[row[i]]:
                if item in seen:
                     wrong_value = item
                     break
                
        if wrong_value is not None:
            index = row.index(wrong_value)
            row.insert(index, row.pop(i))
            redos += 1
            i = 0
            seen = set()
        else: 
            seen.add(row[i])
            i += 1



    if redos:
        l.append(1)
    else:
        l.append(0)


cnt = 0

for i in range(len(numbers)):
     
     if l[i]:
        mid = (len(numbers[i])+1)//2
        cnt += numbers[i][mid-1]

print(cnt)
     




                     
                
            
          
    
     

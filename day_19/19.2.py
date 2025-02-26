file_path = 'input.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

    variables = lines[0].strip().split(', ')

    options = [line.strip() for line in lines[1:] if line.strip()]


variables = set(variables)
# print('Variables:', variables)
# print('options', options)

def recur(option,l,start,seen):
    # print(l)
    

    if start == len(l):
        return 1
    
    val = 0
    for i in range(start,len(l)):

        if option[start:i+1] in variables:

            if i+1<len(l) and i+1 in seen:
                val += l[i+1]
            else:
                val += recur(option,l,i+1,seen)

    l[start] = val
    seen.add(start)
    return val


    
truth = []


cnt = 0
n = len(options)
for option in options:
    cnt += 1

    l = [0 for i in range(len(option))]

    recur(option,l,0,set())

    truth.append(l[0])


print(sum(truth))




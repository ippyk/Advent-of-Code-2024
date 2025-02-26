s = ''

with open('input.txt', 'r') as file:
        for line in file:
            s += line

stack = ['m','u','l','(',',',')']

stack2= ['d','o','(',')']

stack3 = ['d','o','n',"'",'t','(',')']


n = len(s)

index = 0
index2 = 0
index3 = 0

total = 0

do = True


l = []
num1 = ''
num2 = ''

for i in range(n):

    if s[i] == stack2[index2]:
        index2 += 1
        if index2 == 4:
            do = True
            index2 = 0
    else:
        index2 = 0

    if s[i] == stack3[index3]:
        index3 += 1
        if index3 == 4:
            do = False
            index3 = 0
    else:
        index3 = 0


    if do and index == 4:
        if s[i] in ['0','1','2','3','4','5','6','7','8','9']:
             num1 += s[i]
             continue
        elif s[i] == ',':
             pass
        
    if do and index == 5:
        if s[i] in ['0','1','2','3','4','5','6','7','8','9']:
             num2 += s[i]
             continue
        elif s[i] == ')':
             pass
      
    if do and s[i] == stack[index]:
        index +=1

        if index == 6:
            if num1 and num2:

                if num1[0] == '0' or num2[0] == '0':
                    pass
                else:
                    total += int(num1) * int(num2)
                    l.append((num1,num2))

            num1 = ''
            num2 = ''
            index = 0

    else:

        index = 0
        num1 = ''
        num2 = ''


print(total)
         
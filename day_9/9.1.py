s = ''

with open('input.txt', 'r') as file:
        cnt = 0
        for line in file:
            cnt += 1
            s += line.strip()

disk = True

l = []
cnt = 0
for i in range(len(s)):
      
    if not disk:
        for j in range(int(s[i])):
            l.append('.')
        disk = True

    else:
        for j in range(int(s[i])):
            l.append(str(cnt))
        cnt += 1
        disk = False

l1 = l.copy()
l2 = l.copy()

l = 0
r = len(l1) - 1

while l < r:
     
    if l1[l] == '.':
        while l1[r] == '.':
            r -= 1
            if l>=r:
                break

        if l>=r:
            break

        l1[l] = l1[r]
        l1[r] = '.'

    l += 1

total = 0

for i in range(len(l1)):

    if l1[i] == '.':
        break

    total += i*int(l1[i])

print(total)




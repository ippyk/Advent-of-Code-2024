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

d_l = {}

start = -1
end = -1

lefts = []

for i in range(len(l1)):

    if (start == -1) and l1[i] == '.':
        start = i
    elif start > -1 and l1[i] == '.':
        continue
    elif start > -1 and l1[i] != '.':
        end = i-1
        lefts.append((start,end,end-start+1))
        start = -1
        end = -1

rights = []

start = -1
end = -1
value = -1

for i in range(len(l1)-1,-1,-1):

    if (start == -1) and l1[i] != '.':
        start = i
        value = l1[i]
    elif start > -1 and l1[i] == value:
        continue
    elif start > -1 and l1[i] != value:
        end = i+1
        rights.append((end,start,start-end+1,value))
        start = -1
        end = -1
        value = -1

        if l1[i] != '.':
            start = i
            value = l1[i]

moved = False

for r in range(len(rights)):

    for l in range(len(lefts)):

        if lefts[l] is None:
            continue

        if lefts[l][1] < rights[r][0]:

            if lefts[l][2] >= rights[r][2]:

                moved = True

                for index in range(rights[r][2]):
                    l1[lefts[l][0]+index] = rights[r][3]
                    l1[rights[r][0]+index] = '.'

                if lefts[l][2] == rights[r][2]:
                    lefts[l] = None
                else:
                    lefts[l] = (lefts[l][0]+rights[r][2],lefts[l][1],lefts[l][2]-rights[r][2])

        if moved:
            break

    if moved:
        moved = False
        continue

total = 0

for i in range(len(l1)):

    if l1[i] == '.':
        continue

    total += i*int(l1[i])

print(total)




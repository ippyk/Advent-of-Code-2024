with open('input.txt', 'r') as file:
    numbers = []
    d = {}
    cnt = 0
    for line in file:
        colon = False
        first_num = ''

        for i in range(len(line)):

            if line[i] == ':':
                colon = True
            
            if not colon:
                first_num += line[i]
            else:
                l = line[i+1:].strip().split(' ')
                break

        d[int(first_num)] = [int(item) for item in l]


l = []
cnt = 0

for num in d:

    items = set()

    for i in range(len(d[num])):

        new_items = set()

        if not items:
            new_items.add(d[num][i])

        else:

            for item in items:

                new_items.add(item + d[num][i])
                new_items.add(item * d[num][i])
                new_items.add(int(str(item) + str(d[num][i])))

        items = new_items

    if num in items:
        cnt += num
        l.append(1)
    else:
        l.append(0)

print(cnt)



            





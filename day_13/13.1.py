import re
import numpy as np

numbers = []
with open('input.txt', 'r') as file:
    paragraph = []
    for line in file:
        if line.strip() == '':
            if paragraph:
                vals = re.findall(r'\d+', ' '.join(paragraph))
                numbers.append(list(map(int, vals)))
                paragraph = []
        else:
            paragraph.append(line.strip())
    
    if paragraph:
        vals = re.findall(r'\d+', ' '.join(paragraph))
        numbers.append(list(map(int, vals)))

total = 0
l = []

for value in numbers:

    vec1 = np.array(value[:2])
    vec2 = np.array(value[2:4])
    target = np.array(value[4:6])
    cnt = 0
    min_cost = float('inf')

    while cnt*vec1[0] <= target[0] and cnt*vec1[1] <= target[1]:

        r1 = (target[0] - cnt*vec1[0]) // vec2[0]
        r2 = (target[1] - cnt*vec1[1]) // vec2[1]
        if (r1==r2) and ((target[0] - cnt*vec1[0]) % vec2[0] == 0) and ((target[1] - cnt*vec1[1]) % vec2[1] == 0):
            min_cost = min(min_cost, cnt*3 + r1)

        cnt += 1

    if min_cost == float('inf'):
        l.append(0)
    else:
        l.append(1)
        total += min_cost

print(total)
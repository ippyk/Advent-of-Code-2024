import re
import numpy as np
import math

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
big_cnt = 0
n  = len(numbers)

for value in numbers:

    big_cnt += 1
    value[4] += 10_000_000_000_000
    value[5] += 10_000_000_000_000

    vec1 = np.array(value[:2])
    vec2 = np.array(value[2:4])
    target = np.array(value[4:6])
    

    matrix = np.array([[vec1[0], vec2[0]], [vec1[1], vec2[1]]])


    determinent = vec1[0]*vec2[1] - vec1[1]*vec2[0]

    if not determinent:
        print('NO DETERMINENT')

    vals = np.linalg.solve(matrix, target)
    tolerance = 1e-4

    if abs(vals[0]-round(vals[0])) <= tolerance and abs(vals[1]-round(vals[1])) <= tolerance and vals[0]>=0 and vals[1]>=0:
        total += 3*vals[0] + vals[1]
    else:
        pass

print(total)
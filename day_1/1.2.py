import numpy as np
from collections import Counter

data = np.loadtxt('input.txt')

data[:,0] = sorted(data[:,0])
data[:,1] = sorted(data[:,1])

cnt = 0

for item in data:

    cnt += abs(item[0]-item[1])

l_dict = Counter(data[:,0])
r_dict = Counter(data[:,1])

cnt2 = 0

for value in l_dict:

    cnt2 += value * r_dict[value]

print(cnt2)


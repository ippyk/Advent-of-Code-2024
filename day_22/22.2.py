from collections import deque

nums = []

with open('input.txt', 'r') as file:

    for line in file:
        nums.append(int(line.strip()))


def next_secret(num, iters):

    seen = set()
    numdict = {}
    storage = deque(maxlen=4)

    for i in range(iters):
        new1 = num * 64
        new_num = num ^ new1
        new_num = new_num % 16777216

        new2 = new_num // 32
        new_num = new_num ^ new2
        new_num = new_num % 16777216

        new3 = new_num * 2048
        new_num = new_num ^ new3
        new_num = new_num % 16777216
        change = int(str(new_num)[-1]) - int(str(num)[-1])
        num = new_num

        storage.append(change)
        if (len(storage)>= 4) and ((storage[0],storage[1],storage[2],storage[3]) not in numdict):
            numdict[(storage[0],storage[1],storage[2],storage[3])] = int(str(new_num)[-1])

    return new_num, numdict

total = 0

dicts = []
for num in nums:
    output, outputdict = next_secret(num, 2000)
    total += output
    dicts.append(outputdict)

first_dict = dicts[0]
value_dict = {}

all_items = set()
for d in dicts:
    all_items.update(d.keys())

n = len(all_items)
cnt = 0


for storage in all_items:
    cnt += 1
    print(cnt/n)

    value_dict[storage] = 0

    for dict in dicts:
        value_dict[storage] += dict.get(storage, 0)

print(max(value_dict.values()))
print('break')


        



vals = []

with open('input.txt', 'r') as file:
    lines = file.readlines()
    
    for line in lines:
        vals.append(line.strip().split('-'))

d_links = {}
cycles = set()
d_links_new = {}

for val in vals:
    if val[0] in d_links:
        d_links[val[0]].add(val[1])
    else:
        d_links[val[0]] = set()
        d_links[val[0]].add(val[1])

    if val[1] in d_links:
        d_links[val[1]].add(val[0])
    else:
        d_links[val[1]] = set()
        d_links[val[1]].add(val[0])

    if val[0] in d_links and val[1] in d_links:
        intersection = d_links[val[0]].intersection(d_links[val[1]])
        if intersection:
            for item in intersection:
                new_item = tuple(sorted([val[0], val[1], item]))
                d_links_new[new_item] = intersection.intersection(d_links[item])

cnt = 0

while d_links_new:
    cnt += 1
    d_links2 = {}

    for val1 in d_links_new:
        val1_set = set(val1)
        for val2 in d_links:

            if val2 in val1_set:
                continue

            if val2 in d_links_new[val1]:
                new_intersection = d_links[val2].intersection(d_links_new[val1])    
                new_item = tuple(sorted(list(val1) + [val2]))
                d_links2[new_item] = new_intersection

    old_links = d_links_new
    d_links_new = d_links2

s = ''
for item in old_links:
    for node in item:
        s += node + ','

s = s[:-1]
print(s)
            









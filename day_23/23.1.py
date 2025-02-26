vals = []

with open('input.txt', 'r') as file:
    lines = file.readlines()
    
    for line in lines:
        vals.append(line.strip().split('-'))

d_links = {}
cycles = set()

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
                trio = sorted([val[0], val[1], item])
                cycles.add(tuple(trio))

t_cycles = set()

for cycle in cycles:

    if cycle[0][0] == 't' or cycle[1][0] == 't' or cycle[2][0] == 't':
        t_cycles.add(cycle)

print(len(t_cycles))







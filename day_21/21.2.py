codes = []

with open('input.txt', 'r') as file:

    for line in file:
        codes.append(line.strip())

numeric_pos = {"7": (0, 0), "8": (0, 1), "9": (0, 2), "4": (1, 0), "5": (1, 1), "6": (1, 2),
               "1": (2, 0), "2": (2, 1), "3": (2, 2), None: (3, 0), "0": (3, 1), "A": (3, 2)}
directional_pos = {None: (0, 0), "^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}


def sanitize_paths(paths, p0, numeric=True):

    excluded_pos = numeric_pos[None] if numeric else directional_pos[None]

    i = 0
    while i < len(paths):
        p = list(p0)
        for d in paths[i]:

            if d == "^":
                p[0] -= 1
            if d == "v":
                p[0] += 1

            if d == "<":
                p[1] -= 1
            if d == ">":
                p[1] += 1
            
            if tuple(p) == excluded_pos:
                paths.pop(i)
                i -= 1
                break
        
        i += 1

    return paths


def get_shortest_paths(src_pos, trg_pos, numeric=True):
    cx = "^" if trg_pos[0] - src_pos[0] < 0 else "v"
    dx = abs(trg_pos[0] - src_pos[0])
    cy = "<" if trg_pos[1] - src_pos[1] < 0 else ">"
    dy = abs(trg_pos[1] - src_pos[1])

    return sanitize_paths(list(set([cx * dx + cy * dy, cy * dy + cx * dx])), src_pos, numeric=numeric)


def solve_numeric(num):
    pos = numeric_pos["A"]

    sequence = []

    for n in num:
        p = numeric_pos[n]
        paths = get_shortest_paths(pos, p, numeric=True)
        pos = p
        sequence.append(paths)
    
    sequence_parts = []
    for part in sequence:
        tmp = []
        for p in part:
            tmp.append("".join(p) + "A")
        
        sequence_parts.append(tmp)

    return sequence_parts


def solve_directional(seq):
    pos = directional_pos["A"]

    sequence = []

    for n in seq:
        p = directional_pos[n]
        paths = get_shortest_paths(pos, p, numeric=False)
        pos = p
        sequence.append(paths)
    
    sequence_parts = []
    for part in sequence:
        tmp = []
        for p in part:
            tmp.append("".join(p) + "A")
        
        sequence_parts.append(tmp)

    return sequence_parts


memory = {}

def min_cost(seq, depth):
    if depth == 0:
        return len(seq)
    
    if (seq, depth) in memory:
        return memory[(seq, depth)]
    
    sub_sequences = solve_directional(seq)

    cost = 0
    for part in sub_sequences:
        cost += min([min_cost(seq, depth-1) for seq in part])
    
    memory[(seq, depth)] = cost
    return cost


def solve():
    """
    Solve level 2
    """

    depth = 25

    tot = 0
    for num in codes:
        sequence = solve_numeric(num)

        seq_tot = 0
        for part in sequence:
            seq_tot += min([min_cost(seq, depth) for seq in part])

        tot += int(num[:-1]) * seq_tot

    return tot

print(solve())
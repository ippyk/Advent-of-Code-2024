from itertools import permutations

codes = []

with open('input.txt', 'r') as file:

    for line in file:
        codes.append(line.strip())

numeric_keypad = [['7', '8', '9'],['4','5','6'],['1','2','3'],['#','0','A']]
d_numeric = {}

for i in range(len(numeric_keypad)):
    for j in range(len(numeric_keypad[i])):
        d_numeric[numeric_keypad[i][j]] = (i,j)

directional_keypad = [['#','^','A'],['<','v','>']]
d_directional = {}

for i in range(len(directional_keypad)):
    for j in range(len(directional_keypad[i])):
        d_directional[directional_keypad[i][j]] = (i,j)

directions = {'^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}

def get_combo(s):

    all_permuations = set(permutations(s))

    combos = [''.join(i) for i in all_permuations]

    return combos

def numeric(test):

    start = 'A'
    possys = set()

    for i in range(len(test)):
        output1 = ''
        output2 = ''

        
        change1 = d_numeric[test[i]][0] -  d_numeric[start][0]
        change2 = d_numeric[test[i]][1] -  d_numeric[start][1]

        if change1 > 0:
            sign = 'v'
        else:
            sign = '^'

        for j in range(abs(change1)):
            output1 += sign

        if change2 > 0:
            sign = '>'
        else:
            sign = '<'

        for j in range(abs(change2)):
            output2 += sign


        if output1 and output2:

            if start == '0' and output2 == '<':
                output_combos = [output1+output2]
            elif start == 'A' and output2 == '<<':
                output_combos = [output1+output2]
            elif test[i] == '0' and output2 == '>':
                output_combos = [output2+output1]
            elif test[i] == 'A' and output2 == '>>':
                output_combos = [output2+output1]
            else:
                output_combos = [output1+output2, output2+output1]
        elif output1:
            output_combos = [output1]
        elif output2:
            output_combos = [output2]
        else:
            output_combos = ['']

        if possys:
            new_possys = set()
            for item in possys:
                for combo in output_combos:
                    new_possys.add(item+combo+'A')
        else:
            new_possys = set()
            for combo in output_combos:
                    new_possys.add(combo+'A')


        possys = new_possys

        start = test[i]

    return possys

def directional(strings):

    start = 'A'
    all_possys = set()

    for string in strings:
        possys = set()

        for i in range(len(string)):
            output1 = ''
            output2 = ''

            
            change1 = d_directional[string[i]][0] -  d_directional[start][0]
            change2 = d_directional[string[i]][1] -  d_directional[start][1]

            if change1 > 0:
                sign = 'v'
            else:
                sign = '^'

            for j in range(abs(change1)):
                output1 += sign

            if change2 > 0:
                sign = '>'
            else:
                sign = '<'

            for j in range(abs(change2)):
                output2 += sign


            if output1 and output2:
                # print('YES')
                if start == '0' and output2 == '<':
                    output_combos = [output1+output2]
                elif start == 'A' and output2 == '<<':
                    output_combos = [output1+output2]
                elif string[i] == '0' and output2 == '>':
                    output_combos = [output2+output1]
                elif string[i] == 'A' and output2 == '>>':
                    output_combos = [output2+output1]
                else:
                    output_combos = [output1+output2, output2+output1]
            elif output1:
                output_combos = [output1]
            elif output2:
                output_combos = [output2]
            else:
                output_combos = ['']

            if possys:
                new_possys = set()
                for item in possys:
                    for combo in output_combos:
                        new_possys.add(item+combo+'A')
            else:
                new_possys = set()
                for combo in output_combos:
                        new_possys.add(combo+'A')


            possys = new_possys

            start = string[i]

        all_possys = all_possys.union(possys)

    return all_possys

def num_extractor(s):

    new_s = ''
    nums = '0123456789'

    for i in range(len(s)):
        if s[i] in nums:
            new_s += s[i]

    return int(new_s)


total = 0
for code in codes:
    output1 = numeric(code)
    for i in range(2):
        output2 = directional(output1)
        output1 = output2
    total += num_extractor(code)*min([len(x) for x in output2])

print(total)

    








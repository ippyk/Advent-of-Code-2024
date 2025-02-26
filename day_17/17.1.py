import re

with open('input.txt', 'r') as file:
    text = file.read()

registers_pattern = re.compile(r'Register (\w): (\d+)')
program_pattern = re.compile(r'Program: ([\d,]+)')

registers = {}
for match in registers_pattern.findall(text):
    registers[match[0]] = int(match[1])

program_match = program_pattern.search(text)
if program_match:
    program = list(map(int, program_match.group(1).split(',')))
else:
    program = []

cnt = 0
n = len(program)

def get_combo(x):

    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x==2:
        return 2
    elif x==3:
        return 3
    elif x==4:
        return registers['A']
    elif x==5:
        return registers['B']
    elif x==6:
        return registers['C']
    elif x==7:
        print('THER IS A PROBLEM B')


output = []

while cnt < n:
    # print(cnt)

    if program[cnt] == 0:

        if cnt+1 < n:
            value = registers['A'] / 2**get_combo(program[cnt+1])
            registers['A'] = int(value)
        cnt += 2

    elif program[cnt] == 1:

        if cnt+1 < n:
            value  = registers['B'] ^ program[cnt+1]
            registers['B'] = value
        cnt += 2

    elif program[cnt] == 2:

        if cnt+1 < n:
            value = get_combo(program[cnt+1]) % 8
            registers['B'] = value
        cnt += 2

    elif program[cnt] == 3:

        if registers['A'] == 0:
            cnt+=2
            continue
        elif cnt+1 < n:
            cnt = program[cnt+1]

    elif program[cnt] == 4:

        value  = registers['B'] ^ registers['C']
        registers['B'] = value
        cnt += 2

    elif program[cnt] == 5:

        if cnt+1 < n:
            value = get_combo(program[cnt+1]) % 8
            output.append(value)
        cnt += 2

    elif program[cnt] == 6:

        if cnt+1 < n:
            value = registers['A'] / 2**get_combo(program[cnt+1])
            registers['B'] = int(value)
        cnt += 2

    elif program[cnt] == 7:

        if cnt+1 < n:
            value = registers['A'] / 2**get_combo(program[cnt+1])
            registers['C'] = int(value)
        cnt += 2

print('output', output)

        






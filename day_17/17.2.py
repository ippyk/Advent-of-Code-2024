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


def get_output():
    cnt = 0
    n = len(program)
    output = []

    while cnt < n:
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

    return output

def reverse_program(program):
    
    current_a = {0}
    reversed_program = program[::-1]

    for item in reversed_program:

        next_a = set()

        for a in current_a:

            new_a = a*8

            for candidate_a in range(new_a, new_a+8):
                registers['A'] = candidate_a
                registers['B'] = 0
                registers['C'] = 0
                output = get_output()
                if output[0] == item:
                    next_a.add(candidate_a)

        current_a = next_a

    return min(current_a)

val = reverse_program(program)
print(val)





        






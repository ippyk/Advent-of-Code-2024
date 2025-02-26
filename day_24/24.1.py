def read_values_and_operations(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    before_empty_line = []
    after_empty_line = []
    current_list = before_empty_line

    for line in lines:
        stripped_line = line.strip()
        if stripped_line == '':
            current_list = after_empty_line
            continue
        current_list.append(stripped_line)

    values = []
    for line in before_empty_line:
        key, value = line.split(': ')
        values.append([key, int(value)])

    operations = []
    for line in after_empty_line:
        parts = line.replace('->', '').strip().split()
        operations.append(parts)

    return values, operations


file_path = 'input.txt'
values, operations = read_values_and_operations(file_path)

d_values = {}
for item in values:
    d_values[item[0]] = item[1]


def compute(value1, value2, operation):

    if operation == 'AND':

        return value1 & value2
    
    elif operation == 'OR':

        return value1 | value2
    
    elif operation == 'XOR':

        if value1 == value2:
            return 0
        else:
            return 1


stack  = [row.copy() for row in operations]

while stack:

    first_item = stack.pop(0)

    if first_item[0] in d_values and first_item[2] in d_values:

        output = compute(d_values[first_item[0]], d_values[first_item[2]], first_item[1])

        d_values[first_item[3]] = output

    else:

        stack.append(first_item)


count = 0
for val in d_values:

    if val[0] == 'z' and d_values[val]:

        count += 2**(int(val[1:]))

print(count)




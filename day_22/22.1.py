nums = []

with open('input.txt', 'r') as file:

    for line in file:
        nums.append(int(line.strip()))


def next_secret(num, iters):


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
        num = new_num

    return new_num

total = 0

for num in nums:
    output = next_secret(num, 2000)
    total += output

print(total)



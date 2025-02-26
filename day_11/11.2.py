with open("input.txt", "r") as file:
    for line in file:
        nums = line.split(' ')
        nums = [int(value) for value in nums]

d= {}

target = 75

def recur(num, iter):

    if iter == target:
        return 1

    if (num, iter) in d:
        return d[(num,iter)]

    if num == 0:
        result = recur(1, iter+1)
        d[(num,iter)] = result
        return result

    elif not len(str(num)) % 2:
        halfway = len(str(num)) // 2
        val1 = int(str(num)[:halfway])
        val2 = int(str(num)[halfway:])

        result = recur(val1, iter+1) + recur(val2, iter+1)
        d[(num, iter)] = result

        return result

    else:

        result = recur(num*2024, iter+1)
        d[(num, iter)] = result
        return result

total = 0

for item in nums:

    total += recur(item, 0)

print(total)


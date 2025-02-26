with open("test.txt", "r") as file:
    for line in file:
        nums = line.split(' ')
        nums = [int(value) for value in nums]

print(nums)

d= {}

def iterate(nums):

    new_l = []

    for i in range(len(nums)):

        if nums[i] in d:
            new_l += d[nums[i]]
            continue

        if nums[i] == 0:
            new_l.append(1)
        elif not len(str(nums[i])) % 2:
            halfway = len(str(nums[i])) // 2
            new_l.append(int(str(nums[i])[:halfway]))
            new_l.append(int(str(nums[i])[halfway:]))
            d[nums[i]] = [int(str(nums[i])[:halfway]),int(str(nums[i])[halfway:])]
        else:
            new_l.append(nums[i]*2024)
            d[nums[i]] = [nums[i]*2024]

    return new_l


cnt = 0

while cnt < 35:
    print(cnt, len(nums))

    print(min(nums), max(nums))

    nums = iterate(nums)
    cnt += 1

print(len(nums))
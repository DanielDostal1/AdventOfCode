with open("./input.txt", "r") as f:
    data = f.read().splitlines()

result = 0
nums = [[], []]

for n in data:
    values = n.split()
    nums[0].append(int(values[0]))
    nums[1].append(int(values[1]))

nums[0].sort()
nums[1].sort()

for i in range(len(nums[0])):
    dif = nums[0][i] - nums[1][i]
    if dif < 0:
        dif = -dif
    result += dif

print(result)

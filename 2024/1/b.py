with open("./input.txt", "r") as f:
    data = f.read().splitlines()

result = 0
nums = [[], []]

for n in data:
    [a, b] = n.split()
    nums[0].append(int(a))
    nums[1].append(int(b))

for i in range(len(nums[0])):
    sim = nums[0][i] * nums[1].count(nums[0][i])
    result += sim

print(result)

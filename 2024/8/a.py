from collections import defaultdict

with open("./input.txt", "r") as f:
    data = f.read().splitlines()

nums = defaultdict(list)

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char != ".":
            nums[char].append((j, i))

nodeSet = set()
for char in nums:
    ns = nums[char]
    for i in range(len(ns)):
        for j in range(i + 1, len(ns)):
            x1, y1 = ns[i]
            x2, y2 = ns[j]
            ny1 = y1 - abs(y2 - y1)
            ny2 = y2 + abs(y2 - y1)
            xdif = abs(x2 - x1)
            nx1 = x1 + xdif if x1 > x2 else x1 - xdif
            nx2 = x2 + xdif if x2 > x1 else x2 - xdif
            if ny1 in range(0, len(data)) and nx1 in range(0, len(data[0])):
                nodeSet.add((nx1, ny1))
            if ny2 in range(0, len(data)) and nx2 in range(0, len(data[0])):
                nodeSet.add((nx2, ny2))

print(len(nodeSet))

import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

with open("./input.txt", "r") as f:
    data = f.read().splitlines()

nums = defaultdict(list)

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char != ".":
            nums[char].append((j, i))

nodeSet = set()


def createNodes(nums):
    newNums = list(nums)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            x1, y1 = nums[i]
            x2, y2 = nums[j]
            ydif = abs(y2 - y1)
            ny1 = y1 + ydif if y1 > y2 else y1 - ydif
            ny2 = y2 + ydif if y2 > y1 else y2 - ydif
            xdif = abs(x2 - x1)
            nx1 = x1 + xdif if x1 > x2 else x1 - xdif
            nx2 = x2 + xdif if x2 > x1 else x2 - xdif
            if ny1 in range(0, len(data)) and nx1 in range(0, len(data[0])):
                if (nx1, ny1) not in newNums:
                    newNums.append((nx1, ny1))
            if ny2 in range(0, len(data)) and nx2 in range(0, len(data[0])):
                if (nx2, ny2) not in newNums:
                    newNums.append((nx2, ny2))
    if len(newNums) > len(nums):
        return createNodes(newNums)
    else:
        return newNums


for char in nums:
    charCoordsList = nums[char]
    for i in range(len(charCoordsList)):
        for j in range(i + 1, len(charCoordsList)):
            for num in createNodes([charCoordsList[i], charCoordsList[j]]):
                nodeSet.add(num)

print(len(nodeSet))


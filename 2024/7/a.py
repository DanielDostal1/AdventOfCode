import sys

sys.setrecursionlimit(10**6)

with open("./input.txt", "r") as f:
    data = f.read().splitlines()


def getPossibilities(values, operations):
    newOperations = set()
    for operation in operations:
        if len(values) == 1:
            newOperations.add(operation + values[0])
            print
        else:
            newOperations.add(operation + values[0] + " + ")
            newOperations.add(operation + values[0] + " * ")
    if len(values) == 1:
        return newOperations
    else:
        return getPossibilities(values[1:], newOperations)


ans = 0

for line in data:
    left, values = line.split(":")
    left = int(left)
    values = values.split()
    operations = list()
    valuesLen = len(values)
    visitedPos = getPossibilities(values, {""})
    for pos in visitedPos:
        pos = pos.split()
        res = int(pos[0])
        for i in range(1, len(pos) - 1, 2):
            op = pos[i]
            num = pos[i + 1]
            if op == "+":
                res += int(num)
            elif op == "*":
                res *= int(num)
        if res == left:
            ans += left
            break

print(ans)


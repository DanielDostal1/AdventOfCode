from collections import defaultdict

with open("./input.txt", "r") as f:
    data = f.read().splitlines()

rules = defaultdict(list)
ans = 0
i = 0

for i in range(len(data)):
    line = data[i]
    if line == "":
        break

    n1, n2 = line.split("|")
    rules[n1].append(n2)


def checkValid(line):
    valid = True
    for num in range(len(line)):
        before = line[:num]
        for rule in rules[line[num]]:
            if rule in before:
                valid = False
    return valid


for j in range(i + 1, len(data)):
    line = data[j].split(",")
    if not checkValid(line):
        newLine = list(line)
        for m in range(len(line)):
            num = newLine[m]
            before = newLine[:m]
            indexes = []
            for rule in rules[num]:
                if rule in before:
                    indexes.append(newLine.index(rule))
            if len(indexes):
                index = min(indexes)
                newLine.remove(num)
                newLine.insert(index, num)
                if checkValid(newLine):
                    ans += int((newLine[int((len(newLine) - 1) / 2)]))
                    break

print(ans)


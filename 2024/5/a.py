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

for j in range(i + 1, len(data)):
    line = data[j].split(",")
    valid = True
    for num in range(len(line)):
        before = line[:num]
        for rule in rules[line[num]]:
            if rule in before:
                valid = False
    if valid:
        ans += int((line[int((len(line) - 1) / 2)]))

print(ans)

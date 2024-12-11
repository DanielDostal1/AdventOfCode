with open("./input.txt", "r") as f:
    data = f.read().splitlines()[0]

files = []
for i, x in enumerate(data):
    if i % 2 == 1:
        files.append([".", int(x)])
    else:
        files.append([str(i // 2), int(x)])

i = len(files) - 1
while True:
    if i < 0:
        break
    f = files[i][:]
    if f[0] == ".":
        i -= 1
        continue
    for j, sp in enumerate(files):
        if sp[0] != "." or j >= i:
            continue
        if sp[1] >= f[1]:
            files[j][1] = sp[1] - f[1]
            files[i][0] = "."
            files.insert(j, f)
            break
    i -= 1

total = 0
i = 0
for k, x in enumerate(files):
    for j in range(x[1]):
        if x[0] != ".":
            numValue = int(x[0]) * i
            total += numValue
        i += 1

print(total)

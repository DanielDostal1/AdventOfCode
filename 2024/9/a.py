with open("./input.txt", "r") as f:
    data = f.readline()

amphipod = ""
amph = []
for i, x in enumerate(data):
    if i % 2 == 1:
        amphipod += "." * int(x)
        for j in range(int(x)):
            amph.append(".")
    else:
        for j in range(int(x)):
            amph.append(str(i // 2))
        amphipod += str(i // 2) * int(x)

i = 0
while i < len(amph):
    if amph[i] == ".":
        if i >= len(amph):
            break
        value = amph[-1]
        while value == ".":
            amph.pop()
            value = amph[-1]
        if i >= len(amph):
            break
        amph[i] = value
        amph.pop()
    i += 1

total = 0
for i, x in enumerate(amph):
    numValue = i * int(x)
    total += numValue

print(total)

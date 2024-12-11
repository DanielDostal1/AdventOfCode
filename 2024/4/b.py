with open("./input.txt", "r") as f:
    data = f.read().splitlines()

count = 0

dirs = [[(1, 1), (-1, -1)], [(1, -1), (-1, 1)]]

for i in range(len(data)):
    for j in range(len(data[i])):
        valid = True
        if data[i][j] != "A":
            valid = False
        for dirGroup in dirs:
            chars = ["M", "S"]
            for dir in dirGroup:
                x = dir[0] + j
                y = dir[1] + i
                if (
                    y in range(0, len(data))
                    and x in range(0, len(data[y]))
                    and data[y][x] in chars
                ):
                    chars.remove(data[y][x])

            if len(chars) != 0:
                valid = False
        if valid:
            count += 1

print(count)


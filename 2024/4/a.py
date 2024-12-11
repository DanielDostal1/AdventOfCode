with open("./input.txt", "r") as f:
    data = f.read().splitlines()

result = 0


def searchInDirection(x, y, dir):
    x2, y2 = dir
    word = "XMAS"
    while len(word):
        if (
            y in range(0, len(data))
            and x in range(0, len(data[y]))
            and data[y][x] == word[0]
        ):
            word = word[1:]
        else:
            return False
        x += x2
        y += y2
    return True


count = 0

dirs = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1), (-1, 1), (1, -1)]

for i in range(len(data)):
    for j in range(len(data[i])):
        for dir in dirs:
            if searchInDirection(j, i, dir):
                count += 1

print(count)


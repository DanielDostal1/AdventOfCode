import sys

sys.setrecursionlimit(10**6)

with open("./input.txt", "r") as f:
    data = f.read().splitlines()

grid = []
for line in data:
    grid.append([])
    for char in line:
        grid[len(grid) - 1].append(char)

ans = 0


def move(pos, d):
    ans = 0

    dx, dy = d
    x, y = pos
    x, y = x + dx, y + dy

    if y not in range(0, len(grid)) or x not in range(0, len(grid[y])):
        return ans
    elif grid[y][x] == "#":
        dirMap = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}
        ans += move(pos, dirMap[d])
    elif grid[y][x] == "." or "X":
        ans += 1 if grid[y][x] == "." else 0
        grid[y][x] = "X"
        ans += move((x, y), d)
    return ans


for y in range(len(grid)):
    x = 0
    d = (0, 0)
    if "^" in grid[y]:
        d = (0, -1)
        x = grid[y].index("^")
    elif ">" in grid[y]:
        d = (1, 0)
        x = grid[y].index(">")
    elif "v" in grid[y]:
        d = (0, 1)
        x = grid[y].index("v")
    elif "<" in grid[y]:
        d = (-1, 0)
        x = grid[y].index("<")

    if d != (0, 0):
        grid[y][x] == "."
        ans += 1
        ans += move((x, y), d)


print(ans)

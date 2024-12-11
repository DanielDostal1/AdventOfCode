import sys

sys.setrecursionlimit(10**8)

with open("./input.txt", "r") as f:
    data = f.read().splitlines()

grid = []
for line in data:
    grid.append([])
    for char in line:
        grid[len(grid) - 1].append(char)

ans = 0


def move(grid, pos, dir, visitedPos):
    ans = 0
    xd, yd = dir
    x, y = pos
    x, y = x + xd, y + yd

    if ((x, y), dir) in visitedPos:
        return ans + 1
    visitedPos.add(((x, y), dir))
    if y not in range(0, len(grid)) or x not in range(0, len(grid[y])):
        return ans
    elif grid[y][x] == "#":
        dirMap = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}
        ans += move(grid, pos, dirMap[dir], visitedPos)
    elif grid[y][x] == "." or "X":
        ans += move(grid, (x, y), dir, visitedPos)
    return ans


x = 0
dir = (0, 0)
for y in range(len(grid)):
    if "^" in grid[y]:
        dir = (0, -1)
        x = grid[y].index("^")
    elif ">" in grid[y]:
        dir = (1, 0)
        x = grid[y].index(">")
    elif "v" in grid[y]:
        dir = (0, 1)
        x = grid[y].index("v")
    elif "<" in grid[y]:
        dir = (-1, 0)
        x = grid[y].index("<")
    if dir != (0, 0):
        grid[y][x] = "."
        break


if dir != (0, 0):
    for k in range(len(grid)):
        for j in range(len(grid[k])):
            if grid[k][j] != "#":
                newGrid = [row[:] for row in grid]
                newGrid[k][j] = "#"
                ans += move(newGrid, (x, y), dir, set())

print(ans)


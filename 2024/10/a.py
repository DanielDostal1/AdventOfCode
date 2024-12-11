data = open("input.txt").read().splitlines()

grid = []
for line in data:
    grid.append([int(num) for num in line])

p1 = 0


def findTrail(grid, pos):
    x, y = pos
    trailHeads = set()
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dir in dirs:
        xd, yd = dir
        xd += x
        yd += y
        if yd in range(0, len(grid)) and xd in range(0, len(grid[yd])):
            if grid[y][x] + 1 == grid[yd][xd]:
                if grid[yd][xd] == 9:
                    trailHeads.add((xd, yd))
                else:
                    theads = findTrail(grid, (xd, yd))
                    for head in theads:
                        trailHeads.add(head)
    return trailHeads


for y in range(len(data)):
    for x in range(len(data[y])):
        if grid[y][x] == 0:
            trailHeads = findTrail(grid, (x, y))
            p1 += len(trailHeads)

print(p1)

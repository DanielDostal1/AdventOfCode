import sys

sys.setrecursionlimit(10**6)

with open("input.txt", "r") as f:
    data = f.read().splitlines()

regions = list()
visitedLocations = set()


def findRegion(data, pos, visitedLocations):
    x, y = pos
    visitedLocations.add(pos)
    char = data[y][x]
    dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for dir in dirs:
        dx, dy = dir
        nx, ny = x + dx, y + dy
        if (
            ny not in range(len(data))
            or nx not in range(len(data[y]))
            or (nx, ny) in visitedLocations
        ):
            continue
        elif data[ny][nx] == char:
            locations = findRegion(data, (nx, ny), visitedLocations)
            [visitedLocations.add(location) for location in locations]
    return visitedLocations


for y, line in enumerate(data):
    for x, char in enumerate(line):
        if (x, y) not in visitedLocations:
            locations = findRegion(data, (x, y), set())
            regions.append(locations)
            [visitedLocations.add(location) for location in locations]

price = 0


for region in regions:
    print(region)
    regionPerimeter = 0
    for location in region:
        x, y = location
        perimeter = 4
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for dir in dirs:
            dx, dy = dir
            if (x + dx, y + dy) in region:
                perimeter -= 1
        regionPerimeter += perimeter
    price += regionPerimeter * len(region)


print(price)

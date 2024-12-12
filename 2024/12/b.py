import sys
from collections import defaultdict

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


def calcSides(data, region):
    sides = 0
    locChecked = defaultdict(set)
    dirs = {
        (1, 0): {(0, 1), (0, -1)},
        (0, 1): {(1, 0), (-1, 0)},
        (-1, 0): {(0, 1), (0, -1)},
        (0, -1): {(1, 0), (-1, 0)},
    }
    for location in region:
        x, y = location
        for dir in dirs:
            dx, dy = dir
            nx, ny = x + dx, y + dy
            if (nx, ny) in region:
                continue
            nx = nx if dx else 0
            ny = ny if dy else 0
            for d in dirs[dir]:
                dx1, dy1 = d
                ndx, ndy = x + dx1, y + dy1
                while True:
                    if (ndx, ndy) not in region:
                        break
                    if (ndx + dx, ndy + dy) in region:
                        break
                    locChecked[(nx, ny)].add((ndx, ndy))
                    ndx += dx1
                    ndy += dy1
            if (x, y) not in locChecked[(nx, ny)]:
                print((x, y), (nx, ny), locChecked[(nx, ny)])
                sides += 1
            locChecked[(nx, ny)].add((x, y))
    return sides


for region in regions:
    for location in region:
        x, y = location
        perimeter = 4
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for dir in dirs:
            dx, dy = dir
            if (x + dx, y + dy) in region:
                perimeter -= 1
    sides = calcSides(data, region)
    price += sides * len(region)


print(price)

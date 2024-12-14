with open("input.txt", "r") as f:
    data = f.read().splitlines()

robots = []

for line in data:
    pos, vel = line.split()
    pos = [int(num) for num in pos.split("=")[1].split(",")]
    vel = [int(num) for num in vel.split("=")[1].split(",")]

    robots.append([pos, vel])

gridWidth = 101
gridHeight = 103
time = 16990


def paintRobots(robots, gridWidth, gridHeight):
    grid = [[" " for _ in range(gridWidth)] for _ in range(gridHeight)]
    for robot in robots:
        [x, y] = robot[0]
        grid[y][x] = "█"
    for line in grid:
        print("|" + "".join(line) + "|")


def checkForNeighbours(robots, gridWidth, gridHeight):
    grid = [[" " for _ in range(gridWidth)] for _ in range(gridHeight)]
    for robot in robots:
        [x, y] = robot[0]
        grid[y][x] = "█"

    count = 0
    for line in grid:
        line = "".join(line)
        if "█████" in line:
            count += 1
    if count > 19:
        paintRobots(robots, gridWidth, gridHeight)
        return True
    else:
        return False


for i in range(time):
    for robot in robots:
        [x, y] = robot[1]
        [posX, posY] = robot[0]
        robot[0] = [(posX + x) % gridWidth, (posY + y) % gridHeight]
    if checkForNeighbours(robots, gridWidth, gridHeight):
        print("Time: " + str(i + 1))

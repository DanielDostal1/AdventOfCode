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
time = 100

quadrants = [0 for _ in range(4)]

for robot in robots:
    [x, y] = robot[1]
    for i in range(time):
        [posX, posY] = robot[0]
        robot[0] = [(posX + x) % gridWidth, (posY + y) % gridHeight]

    [posX, posY] = robot[0]
    if posX < gridWidth // 2:
        if posY < gridHeight // 2:
            quadrants[0] += 1
        elif posY > gridHeight // 2:
            quadrants[1] += 1
    elif posX > gridWidth // 2:
        if posY < gridHeight // 2:
            quadrants[2] += 1
        elif posY > gridHeight // 2:
            quadrants[3] += 1

res = 1
for quad in quadrants:
    res *= quad
print(res)

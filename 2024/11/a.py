with open("input.txt", "r") as f:
    data = [int(num) for num in f.readline().split()]


def simulateBlink(data):
    newD = list()
    for num in data:
        sNum = str(num)
        numLen = len(sNum)
        if num == 0:
            newD.append(1)
        elif numLen % 2 == 0:
            n1 = int(sNum[numLen // 2 :])
            n2 = int(sNum[: (numLen // 2)])
            newD.append(n1)
            newD.append(n2)
        else:
            newD.append(num * 2024)
    return newD


blinks = 25
for i in range(blinks):
    data = simulateBlink(data)
    print(i)


print(len(data))

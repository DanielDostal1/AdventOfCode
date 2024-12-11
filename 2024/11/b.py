from collections import defaultdict

with open("input.txt", "r") as f:
    data = [int(num) for num in f.readline().split()]


def simulateBlink(dataDic):
    nDataDic = defaultdict(lambda: 0, dataDic)
    for num in dataDic:
        occurances = dataDic[num]
        nDataDic[num] -= occurances
        if nDataDic[num] == 0:
            del nDataDic[num]
        sNum = str(num)
        numLen = len(sNum)
        if num == 0:
            nDataDic[1] += occurances
        elif numLen % 2 == 0:
            n1 = int(sNum[numLen // 2 :])
            n2 = int(sNum[: (numLen // 2)])
            nDataDic[n1] += occurances
            nDataDic[n2] += occurances
        else:
            nDataDic[num * 2024] += occurances
    return nDataDic


dataDic = defaultdict(lambda: 0)
for num in data:
    dataDic[num] += 1

blinks = 75
for i in range(blinks):
    dataDic = simulateBlink(dataDic)

total = 0
for num in dataDic:
    total += dataDic[num]

print(total)

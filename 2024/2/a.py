with open("./input.txt", "r") as f:
    data = f.read().splitlines()

result = 0


def checkLine(line):
    for i in range(len(line)):
        newLine = line[:i] + line[i + 1 :]
        deacrase = True
        increase = True
        for i in range(1, len(newLine)):
            if newLine[i] > newLine[i - 1] and newLine[i] < newLine[i - 1] + 4:
                print
            else:
                increase = False
            if newLine[i] < newLine[i - 1] and newLine[i] > newLine[i - 1] - 4:
                print
            else:
                deacrase = False
        if increase and not deacrase or deacrase and not increase:
            return True
    return False


for n in data:
    line = [int(num) for num in n.split()]
    result += 1 if checkLine(line) else 0


print(result)

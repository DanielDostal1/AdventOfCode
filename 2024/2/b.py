with open("./input.txt", "r") as f:
    data = f.read().splitlines()

result = 0


def checkLine(line, edited):
    deacrase = True
    increase = True
    for i in range(1, len(line)):
        if line[i] > line[i - 1] and line[i] < line[i - 1] + 4:
            print
        else:
            increase = False
            if not deacrase:
                line.pop(i)
                if edited:
                    return False
                return checkLine(line, True)
        if line[i] < line[i - 1] and line[i] > line[i - 1] - 4:
            print
        else:
            deacrase = False
            if not increase:
                line.pop(i)
                if edited:
                    return False
                return checkLine(line, True)
    if increase and not deacrase or deacrase and not increase:
        return True
    else:
        return False


for n in data:
    line = [int(num) for num in n.split()]
    result += 1 if checkLine(line, False) else 0


print(result)

with open("./input.txt", "r") as f:
    data = f.read().splitlines()

result = 0

enabled = True

for line in range(len(data)):
    line = data[line]
    line = line.split("mul(")
    for j in range(len(line)):
        n = line[j]
        num1, num2 = "", ""
        middle = ""
        if enabled:
            for i in range(len(n)):
                char = n[i]
                if char.isdigit():
                    if middle == "":
                        num1 += char
                    else:
                        num2 += char
                else:
                    if middle == "":
                        middle += char
                    else:
                        break
            if middle == "," and n[i] == ")":
                result += int(num1) * int(num2)
        for i in range(len(n)):
            if i < len(n) + 3 and n[i : i + 4] == "do()":
                enabled = True
            if i < len(n) + 6 and n[i : i + 7] == "don't()":
                enabled = False

print(result)


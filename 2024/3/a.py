with open("./input.txt", "r") as f:
    data = f.read().splitlines()

result = 0
muls = []

for line in data:
    line = line.split("mul(")
    for n in line:
        num1, num2 = "", ""
        middle = ""
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


print(result)


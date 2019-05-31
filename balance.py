from random import randint

with open("data.csv", encoding="utf-8") as f:
    lines = f.readlines()
    female = 0
    male = 0
    infant = 0
    for line in lines:
        if line.lower().strip("\n").split(",")[0] == "1":
            male += 1
        elif line.lower().strip("\n").split(",")[0] == "2":
            female += 1
        elif line.lower().strip("\n").split(",")[0] == "0":
            infant += 1
    while female != male:
        line = lines[randint(0, len(lines)-1)]
        if line.lower().strip("\n").split(",")[0] == "2":
            lines.append(line)
            female += 1
    while infant != male:
        line = lines[randint(0, len(lines)-1)]
        if line.lower().strip("\n").split(",")[0] == "0":
            lines.append(line)
            infant += 1
            
with open("data.csv", mode="w", encoding="utf-8") as f:
    for line in lines:
        f.write(line)

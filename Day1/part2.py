lines = []
with open("Day1/input.txt", "r", encoding="utf-8") as file:
    lines += file.readlines()

val = 50
total_zeros = 0
for line in lines:
    dir = line[0]
    cmd = int(line[1:])
    adder = 0
    printstr = f"{val} {dir} {cmd}"

    if cmd > 100:
        adder += int(cmd / 100)
        cmd = cmd % 100

    if dir == "L":
        if cmd >= val and val != 0:
            adder += 1
        val -= cmd
    else:
        val += cmd
        if val >= 100:
            adder += 1
    val = val % 100

    print(f"{printstr} +{adder}")
    total_zeros += adder
print(val)
print(total_zeros)

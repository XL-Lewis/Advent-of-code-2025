lines = []
with open("Day1/input.txt", "r", encoding="utf-8") as file:
    lines += file.readlines()

val = 50
total_zeros = 0
for line in lines:
    dir = line[0]
    cmd = int(line[1:])
    if dir == "L":
        val -= cmd
    else:
        val += cmd
    val = val % 100
    if val == 0:
        total_zeros += 1

print(val)
print(total_zeros)

import re

with open ("3/input.txt", "r") as file:
    data = file.read()

# find all mul(a,b) in the data where a and b are integers with 1-3 digits
data = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)

total = 0

for i in data:
    total += int(i[0]) * int(i[1])

print("part 1: " + str(total))

with open ("3/input.txt", "r") as file:
    data = file.read()

data = re.findall(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))", data)

total = 0
do = True

for i in data:
    if "do()" in i[0]:
        do = True
    elif "don't()" in i[0]:
        do = False
    elif do:
        total += int(i[1]) * int(i[2])

print("part 2: " + str(total))
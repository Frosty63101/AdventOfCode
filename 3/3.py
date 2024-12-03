import re

# part 1
with open ("3/input.txt", "r") as file:
    data = file.read()

data = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)

total = 0

for i in data:
    total += int(i[0]) * int(i[1])

print("part 1: " + str(total))

# part 2
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

# part 1 (non-regex)
with open ("3/input.txt", "r") as file:
    data = file.read()

s = ""
li = []
dig = 0
n = "m"

for i in data:
    if i == "m" and n == "m":
        s += i
        dig = 0
        n = "u"
    elif i == "u" and n == "u":
        s += i
        dig = 0
        n = "l"
    elif i == "l" and n == "l":
        s += i
        dig = 0
        n = "("
    elif i == "(" and n == "(":
        s += i
        dig = 0
        n = "d1"
    elif i in "1234567890" and dig < 3 and n == "d1":
        s += i
        dig += 1
        if dig == 3:
            n = ","
    elif i == "," and ( n == "," or n == "d1" ):
        s += i
        dig = 0
        n = "d2"
    elif i in "1234567890" and dig < 3 and n == "d2":
        s += i
        dig += 1
        if dig == 3:
            n = ")"
    elif i == ")" and ( n == ")" or n == "d2" ):
        s += i
        li.append(s)
        s = ""
        n = "m"
    else:
        s = ""
        n = "m"

total = 0

for i in li:
    i = i[4:-1].split(",")
    total += int(i[0]) * int(i[1])

print("part 1: " + str(total) + "(non-regex)")

# part 2 (non-regex)
with open ("3/input.txt", "r") as file:
    data = file.read()

s = ""
li = []
dig = 0
n = "md"

for i in data:
    if i == "m" and n == "m":
        s += i
        dig = 0
        n = "u"
    elif i == "u" and n == "u":
        s += i
        dig = 0
        n = "l"
    elif i == "l" and n == "l":
        s += i
        dig = 0
        n = "("
    elif i == "(" and n == "(":
        s += i
        dig = 0
        n = "d1"
    elif i in "1234567890" and dig < 3 and n == "d1":
        s += i
        dig += 1
        if dig == 3:
            n = ","
    elif i == "," and ( n == "," or n == "d1" ):
        s += i
        dig = 0
        n = "d2"
    elif i in "1234567890" and dig < 3 and n == "d2":
        s += i
        dig += 1
        if dig == 3:
            n = ")"
    elif i == ")" and ( n == ")" or n == "d2" ):
        s += i
        li.append(s)
        s = ""
        n = "m"
    elif i == "d" and n == "m":
        s += i
        dig = 0
        n = "o"
    elif i == "o" and n == "o":
        s += i
        dig = 0
        n = "d("
    elif i == "(" and n == "d(":
        s += i
        dig = 0
        n = "d)"
    elif i == ")" and n == "d)":
        s += i
        li.append(s)
        s = ""
        n = "m"
    elif i == "n" and n == "d(":
        s += i
        dig = 0
        n = "'"
    elif i == "'" and n == "'":
        s += i
        dig = 0
        n = "t"
    elif i == "t" and n == "t":
        s += i
        dig = 0
        n = "dn("
    elif i == "(" and n == "dn(":
        s += i
        dig = 0
        n = "dn)"
    elif i == ")" and n == "dn)":
        s += i
        li.append(s)
        s = ""
    else:
        s = ""
        n = "m"

total = 0
do = True

for i in li:
    if i[0] == "m" and do:
        i = i[4:-1].split(",")
        total += int(i[0]) * int(i[1])
    if i[0] == "d":
        if i[2] == "n":
            do = False
        else:
            do = True
        total += 0

print("part 2: " + str(total) + "(non-regex)")
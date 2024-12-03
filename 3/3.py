import re

# part 1
with open ("3/input.txt", "r") as file:
    data = file.read()

data = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)

total1 = 0

for i in data:
    total1 += int(i[0]) * int(i[1])

print("part 1: " + str(total1))

# part 2
with open ("3/input.txt", "r") as file:
    data = file.read()

data = re.findall(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))", data)

total2 = 0
do = True

for i in data:
    if "do()" in i[0]:
        do = True
    elif "don't()" in i[0]:
        do = False
    elif do:
        total2 += int(i[1]) * int(i[2])

print("part 2: " + str(total2))

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

total3 = 0

for i in li:
    i = i[4:-1]
    k = ["", ""]
    p = 0
    for j in i:
        if j == ",":
            p += 1
            continue
        k[p] += j
    total3 += int(k[0]) * int(k[1])

print("part 1: " + str(total3) + " (non-regex and without split)")

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

total4 = 0
do = True

for i in li:
    if i[0] == "m" and do:
        i = i[4:-1]
        k = ["", ""]
        p = 0
        for j in i:
            if j == ",":
                p += 1
                continue
            k[p] += j
        total4 += int(k[0]) * int(k[1])
    if i[0] == "d":
        if i[2] == "n":
            do = False
        else:
            do = True
        total4 += 0

print("part 2: " + str(total4) + " (non-regex and without split)")

print("part 1: ", "test success" if total1 == total3 else "test fail")
print("part 2: ", "test success" if total2 == total4 else "test fail")
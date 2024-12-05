with open("5/input.txt", "r") as file:
    data1, data2 = file.read().split("\n\n")

data1 = data1.split("\n")
data2 = data2.split("\n")

correct = []
flag = False

for pages in data2:
    accept1 = False
    for order in data1:
        page1, page2 = order.split("|")
        if page1 in pages and page2 in pages:
            index1 = -1
            index2 = -1
            pagesl = pages.split(",")
            for i in range(len(pagesl)):
                if pagesl[i] == page1:
                    index1 = i
                if pagesl[i] == page2:
                    index2 = i
            if index1 < index2:
                accept1 = True
            else:
                accept1 = False
                break
    if accept1:
        correct.append(pages)

total = 0

for c in correct:
    n = 0
    for i in c.split(","):
        n += 1
    n -= 1
    if n % 2 == 0:
        n = n // 2
    else:
        n = n // 2 + 1
    total += int(c.split(",")[n])

print("Part 1: " + str(total))


with open("5/input.txt", "r") as file:
    data1, data2 = file.read().split("\n\n")

data1 = data1.strip().split("\n") 
data2 = data2.strip().split("\n") 

incorrect = []

pagesindex = 0 

while pagesindex < len(data2):
    original_pages = data2[pagesindex].strip()
    pagesl = original_pages.split(",") 
    swapped = False 

    while True:
        swapped = False
        for order in data1:
            page1, page2 = order.split("|")
            if page1 in pagesl and page2 in pagesl:
                index1 = pagesl.index(page1)
                index2 = pagesl.index(page2)
                if index1 > index2:
                    pagesl[index1], pagesl[index2] = pagesl[index2], pagesl[index1]
                    swapped = True
        if not swapped:
            break 

    if original_pages != ",".join(pagesl):
        incorrect.append(",".join(pagesl))

    pagesindex += 1

total = 0

for c in incorrect:
    n = 0
    for i in c.split(","):
        n += 1
    n -= 1
    if n % 2 == 0:
        n = n // 2
    else:
        n = n // 2 + 1
    total += int(c.split(",")[n])
print("Part 2:", total)

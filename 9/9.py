with open('9/input.txt', 'r') as file:
    data = file.read().strip()

diskMap = []

for i in range(len(data)):
    if i % 2 == 0:
        diskMap += ([str(i // 2) for _ in range(int(data[i]))])
    else:
        diskMap += (['.' for _ in range(int(data[i]))])

for i in range(len(diskMap)):
    if diskMap[i] == '.':
        for j in range(len(diskMap)-1, i, -1):
            if diskMap[j] != '.':
                diskMap[i] = diskMap[j]
                diskMap[j] = '.'
                break

checksum = 0

for i in range(len(diskMap)):
    if diskMap[i] != '.':
        checksum += i * int(diskMap[i])

print("Part 1: " + str(checksum))


with open('9/input.txt', 'r') as file:
    data = file.read().strip()

diskMap = []

for i in range(len(data)):
    if i % 2 == 0:
        diskMap += ([str(i // 2) for _ in range(int(data[i]))])
    else:
        diskMap += (['.' for _ in range(int(data[i]))])

setDiskMap = set()

for i in range(len(diskMap) - 1, -1, -1):
    if diskMap[i] != '.' and diskMap[i] not in setDiskMap:
        setDiskMap.add(diskMap[i])
        fileLabel = diskMap[i]
        fileLen = 0
        for j in range(i, -1, -1):
            if diskMap[j] != fileLabel:
                break
            fileLen += 1
        freeLen = 0
        for k in range(i):
            if diskMap[k] == '.':
                freeLen += 1
            else:
                freeLen = 0
            if freeLen == fileLen:
                for l in range(fileLen):
                    diskMap[k-freeLen+l+1] = fileLabel
                for m in range(i, i-fileLen, -1):
                    diskMap[m] = '.'
                break

checksum = 0

for i in range(len(diskMap)):
    if diskMap[i] != '.':
        checksum += i * int(diskMap[i])

print("Part 2: " + str(checksum))

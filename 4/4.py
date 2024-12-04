with open("4/input.txt", "r") as file:
    data = file.read().split("\n")

arr = []
for i in data:
    arr.append([j for j in i])

count = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == "X":
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if j + 3*l < len(arr[i]) and j + 3*l >= 0 and i + 3*k < len(arr) and i + 3*k >= 0:
                        if arr[i + k][j + l] == "M":
                            if arr[i + 2*k][j + 2*l] == "A":
                                if arr[i + 3*k][j + 3*l] == "S":
                                    count += 1

print("part 1: " + str(count))

with open("4/input.txt", "r") as file:
    data = file.read().split("\n")

arr = []
for i in data:
    arr.append([j for j in i])

count = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == "A" and i - 1 >= 0 and j - 1 >= 0 and i + 1 < len(arr) and j + 1 < len(arr[i]):
            if (arr[i-1][j-1] == "M" and arr[i+1][j+1] == "S" and arr[i-1][j+1] == "M" and arr[i+1][j-1] == "S") or \
            (arr[i-1][j-1] == "S" and arr[i+1][j+1] == "M" and arr[i-1][j+1] == "S" and arr[i+1][j-1] == "M") or \
            (arr[i-1][j-1] == "M" and arr[i+1][j+1] == "S" and arr[i-1][j+1] == "S" and arr[i+1][j-1] == "M") or \
            (arr[i-1][j-1] == "S" and arr[i+1][j+1] == "M" and arr[i-1][j+1] == "M" and arr[i+1][j-1] == "S"):
                count += 1

print("part 2: " + str(count))
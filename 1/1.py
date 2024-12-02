import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from util.SortAndSearch import *

with open('1/input.txt') as f:
    data = f.read().strip()

l1 = []
l2 = []

for line in data.split('\n'):
    t1, t2 = line.split('   ')
    t1 = int(t1.strip())
    t2 = int(t2.strip())
    l1.append(t1)
    l2.append(t2)

l1 = mergeSort(l1)
l2 = mergeSort(l2)

output = 0

for i in range(len(l1)):
    dif = l1[i] - l2[i]
    if dif < 0:
        dif *= -1
    output += dif

print("Part 1: " + str(output))

# Part 2
output = 0

for i in l1:
    for j in l2:
        n = 0
        if i == j:
            n += 1
        output += i * n

print("Part 2: " + str(output))

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if isinstance(other, Coord):
            return self.x == other.x and self.y == other.y
        return False
    
    def __hash__(self):
        return hash((self.x, self.y))

class Node:
    def __init__(self, coords: list, symbol: str):
        self.amount = len(coords)
        self.coords = coords
        self.symbol = symbol
    
    def add(self, coord: Coord):
        self.amount += 1
        self.coords.append(coord)

with open('8/input.txt', 'r') as file:
    data = file.read().splitlines()

matrix = []

for line in data:
    matrix.append([char for char in line])

symbols = {}

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != '.':
            if matrix[i][j] not in symbols:
                symbols[matrix[i][j]] = Node([Coord(j, i)], matrix[i][j])
            else:
                symbols[matrix[i][j]].add(Coord(j, i))

intersections = set()

for symbol in symbols.keys():
    for node in symbols[symbol].coords:
        for otherNode in symbols[symbol].coords:
            if otherNode != node:
                dx = otherNode.x - node.x
                dy = otherNode.y - node.y
                newNode = Coord(otherNode.x + dx, otherNode.y + dy)
                if newNode.x >= 0 and newNode.x < len(matrix[0]) and newNode.y >= 0 and newNode.y < len(matrix):
                    intersections.add(newNode)

m = []

for i in range(len(matrix)):
    m.append([])
    for j in range(len(matrix[i])):
        m[i].append(matrix[i][j])

for intersection in intersections:
    if m[intersection.y][intersection.x] == '.':
        m[intersection.y][intersection.x] = '#'
    else: 
        m[intersection.y][intersection.x] = 'X'

print("Part 1: " + str(len(intersections)))

with open('8/input.txt', 'r') as file:
    data = file.read().splitlines()

matrix = []

for line in data:
    matrix.append([char for char in line])

symbols = {}

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != '.':
            if matrix[i][j] not in symbols:
                symbols[matrix[i][j]] = Node([Coord(j, i)], matrix[i][j])
            else:
                symbols[matrix[i][j]].add(Coord(j, i))

intersections = set()

for symbol in symbols.keys():
    for node in symbols[symbol].coords:
        for otherNode in symbols[symbol].coords:
            if otherNode != node:
                dx = otherNode.x - node.x
                dy = otherNode.y - node.y
                for n in range(0, len(matrix) + len(matrix[0])):
                    newNode = Coord(otherNode.x + (n * dx), otherNode.y + (n * dy))
                    if newNode.x >= 0 and newNode.x < len(matrix[0]) and newNode.y >= 0 and newNode.y < len(matrix):
                        intersections.add(newNode)

m = []

for i in range(len(matrix)):
    m.append([])
    for j in range(len(matrix[i])):
        m[i].append(matrix[i][j])

for intersection in intersections:
    if m[intersection.y][intersection.x] == '.':
        m[intersection.y][intersection.x] = '#'
    else: 
        m[intersection.y][intersection.x] = 'X'

print("Part 2: " + str(len(intersections)))
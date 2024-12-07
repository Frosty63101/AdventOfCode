from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False
    
    def __repr__(self):
        return f"Position(x={self.x}, y={self.y})"
    
    def __hash__(self):
        return hash((self.x, self.y))

with open('6/input.txt') as file:
    data = file.read().split('\n')

m = []
for line in data:
    m.append([x for x in line])

direction = Enum('Direction', [('UP', 1), ('DOWN', 2), ('LEFT', 3), ('RIGHT', 4)])
p = Position(0, 0)

for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == "^":
            print(i, j)
            direction = Direction.UP
            p.x = j
            p.y = i

track = []

for i in range(len(m)):
    track.append([False] * len(m[0]))

track[p.y][p.x] = True

total = 1

while True:
    if direction == Direction.UP:
        if p.y > 0 and m[p.y - 1][p.x] != "#":
            m[p.y][p.x] = "x"
            p.y -= 1
            m[p.y][p.x] = "^"
        elif p.y > 0 and m[p.y - 1][p.x] == "#":
            direction = Direction.RIGHT
            m[p.y][p.x] = ">"
        else:
            break
    elif direction == Direction.DOWN:
        if p.y < len(m) - 1 and m[p.y + 1][p.x] != "#":
            m[p.y][p.x] = "x"
            p.y += 1
            m[p.y][p.x] = "v"
        elif p.y < len(m) - 1 and m[p.y + 1][p.x] == "#":
            direction = Direction.LEFT
            m[p.y][p.x] = "<"
        else:
            break
    elif direction == Direction.LEFT:
        if p.x > 0 and m[p.y][p.x - 1] != "#":
            m[p.y][p.x] = "x"
            p.x -= 1
            m[p.y][p.x] = "<"
        elif p.x > 0 and m[p.y][p.x - 1] == "#":
            direction = Direction.UP
            m[p.y][p.x] = "^"
        else:
            break
    elif direction == Direction.RIGHT:
        if p.x < len(m[0]) - 1 and m[p.y][p.x + 1] != "#":
            m[p.y][p.x] = "x"
            p.x += 1
            m[p.y][p.x] = ">"
        elif p.x < len(m[0]) - 1 and m[p.y][p.x + 1] == "#":
            direction = Direction.DOWN
            m[p.y][p.x] = "v"
        else:
            break
    
    if not track[p.y][p.x]:
        track[p.y][p.x] = True
        total += 1


print("Part 1: " + str(total))


with open('6/input.txt') as file:
    data = file.read().split('\n')

m = []
for line in data:
    m.append([x for x in line])

direction = Enum('Direction', [('UP', 1), ('DOWN', 2), ('LEFT', 3), ('RIGHT', 4)])
p = Position(0, 0)

for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == "^":
            print(i, j)
            direction = Direction.UP
            p.x = j
            p.y = i

track = []

for i in range(len(m)):
    track.append([False] * len(m[0]))

track[p.y][p.x] = True

total = 1

while True:
    if direction == Direction.UP:
        if p.y > 0 and m[p.y - 1][p.x] != "#":
            m[p.y][p.x] = "x"
            p.y -= 1
            m[p.y][p.x] = "^"
        elif p.y > 0 and m[p.y - 1][p.x] == "#":
            direction = Direction.RIGHT
            m[p.y][p.x] = ">"
        else:
            break
    elif direction == Direction.DOWN:
        if p.y < len(m) - 1 and m[p.y + 1][p.x] != "#":
            m[p.y][p.x] = "x"
            p.y += 1
            m[p.y][p.x] = "v"
        elif p.y < len(m) - 1 and m[p.y + 1][p.x] == "#":
            direction = Direction.LEFT
            m[p.y][p.x] = "<"
        else:
            break
    elif direction == Direction.LEFT:
        if p.x > 0 and m[p.y][p.x - 1] != "#":
            m[p.y][p.x] = "x"
            p.x -= 1
            m[p.y][p.x] = "<"
        elif p.x > 0 and m[p.y][p.x - 1] == "#":
            direction = Direction.UP
            m[p.y][p.x] = "^"
        else:
            break
    elif direction == Direction.RIGHT:
        if p.x < len(m[0]) - 1 and m[p.y][p.x + 1] != "#":
            m[p.y][p.x] = "x"
            p.x += 1
            m[p.y][p.x] = ">"
        elif p.x < len(m[0]) - 1 and m[p.y][p.x + 1] == "#":
            direction = Direction.DOWN
            m[p.y][p.x] = "v"
        else:
            break
    
    if not track[p.y][p.x]:
        track[p.y][p.x] = True
        total += 1

path = []

for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == "x" or m[i][j] == "^" or m[i][j] == "v" or m[i][j] == "<" or m[i][j] == ">":
            path.append(Position(j, i))

with open('6/input.txt') as file:
    data = file.read().split('\n')

m = []
for line in data:
    tmp = []
    for c in line:
        tmp.append(c)
    m.append(tmp)

total = 0
for position in path:
    with open('6/input.txt') as file:
        data = file.read().split('\n')

    m = []
    for line in data:
        tmp = []
        for c in line:
            tmp.append(c)
        m.append(tmp)


    direction = Enum('Direction', [('UP', 1), ('DOWN', 2), ('LEFT', 3), ('RIGHT', 4)])
    p = Position(0, 0)

    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == "^":
                direction = Direction.UP
                p.x = j
                p.y = i

    track = []

    track = [[[False, []] for _ in range(len(m[0]))] for _ in range(len(m))]

    track[p.y][p.x] = [True, [direction]]
    endFlag = False
    
    p = Position(p.x, p.y)
    if m[position.y][position.x] == "#":
        continue
    m[position.y][position.x] = "#" if m[position.y][position.x] != "#" else m[position.y][position.x]
    while True:
        flag = False
        if direction == Direction.UP:
            if p.y > 0 and m[p.y - 1][p.x] != "#":
                m[p.y][p.x] = "x"
                p.y -= 1
                m[p.y][p.x] = "^"
            elif p.y > 0 and m[p.y - 1][p.x] == "#":
                if p.y - 1 == position.y and p.x == position.x:
                    flag = True
                direction = Direction.RIGHT
                m[p.y][p.x] = ">"
            else:
                break
        elif direction == Direction.DOWN:
            if p.y < len(m) - 1 and m[p.y + 1][p.x] != "#":
                m[p.y][p.x] = "x"
                p.y += 1
                m[p.y][p.x] = "v"
            elif p.y < len(m) - 1 and m[p.y + 1][p.x] == "#":
                if p.y + 1 == position.y and p.x == position.x:
                    flag = True
                direction = Direction.LEFT
                m[p.y][p.x] = "<"
            else:
                break
        elif direction == Direction.LEFT:
            if p.x > 0 and m[p.y][p.x - 1] != "#":
                m[p.y][p.x] = "x"
                p.x -= 1
                m[p.y][p.x] = "<"
            elif p.x > 0 and m[p.y][p.x - 1] == "#":
                if p.x - 1 == position.x and p.y == position.y:
                    flag = True
                direction = Direction.UP
                m[p.y][p.x] = "^"
            else:
                break
        elif direction == Direction.RIGHT:
            if p.x < len(m[0]) - 1 and m[p.y][p.x + 1] != "#":
                m[p.y][p.x] = "x"
                p.x += 1
                m[p.y][p.x] = ">"
            elif p.x < len(m[0]) - 1 and m[p.y][p.x + 1] == "#":
                if p.x + 1 == position.x and p.y == position.y:
                    flag = True
                direction = Direction.DOWN
                m[p.y][p.x] = "v"
            else:
                break
        modx = 0
        mody = 0
        if direction == Direction.UP:
            modx = 0
            mody = -1
        elif direction == Direction.DOWN:
            modx = 0
            mody = 1
        elif direction == Direction.LEFT:
            modx = -1
            mody = 0
        elif direction == Direction.RIGHT:
            modx = 1
            mody = 0
        if not track[p.y][p.x][0]:
            track[p.y][p.x][0] = True
            track[p.y][p.x][1].append(direction)
        elif p.y + mody >= 0 and p.y + mody < len(track) and p.x + modx >= 0 and p.x + modx < len(track[0]) and \
        track[p.y][p.x][0] and direction in track[p.y + mody][p.x + modx][1]:
            total += 1
            break
        else:
            track[p.y][p.x][1].append(direction)
    if endFlag:
        break

print("Part 2: " + str(total))
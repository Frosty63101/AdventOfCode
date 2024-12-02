with open('2/input.txt') as f:
    lines = f.readlines()

safe = 0

for line in lines:
    previous = 0
    increasing = True
    unsafe = False
    count = 0
    for t in line.split(' '):
        count += 1
        if count == 2:
            if int(t) < previous:
                increasing = False
            else:
                increasing = True
        if count == 1:
            previous = int(t)
            continue
        if increasing and int(t) < previous:
            unsafe = True
        if not increasing and int(t) > previous:
            unsafe = True
        if increasing:
            if int(t) - 3 > previous:
                unsafe = True
                break
            if int(t) == previous:
                unsafe = True
                break
        else:
            if int(t) + 3 < previous:
                unsafe = True
                break
            if int(t) == previous:
                unsafe = True
        previous = int(t)
    if unsafe:
        continue
    safe += 1

print("part 1: " + str(safe))



with open('2/input.txt') as f:
    lines = f.readlines()

safe = 0

for line in lines:
    unsafe = True
    line = line.strip().split(' ')
    unsafe = True
    for i in range(-1, len(line)):
        previous = 0
        increasing = True
        count = 0
        check = True
        if i == -1:
            print(line)
            for t in range(len(line)):
                count += 1
                if count == 2:
                    if int(line[t]) < previous:
                        increasing = False
                    else:
                        increasing = True
                if count == 1:
                    previous = int(line[t])
                    continue
                if increasing and int(line[t]) < previous:
                    check = False
                    break
                if not increasing and int(line[t]) > previous:
                    check = False
                    break
                if increasing:
                    if int(line[t]) - 3 > previous:
                        check = False
                        break
                    if int(line[t]) == previous:
                        check = False
                        break
                else:
                    if int(line[t]) + 3 < previous:
                        check = False
                        break
                    if int(line[t]) == previous:
                        check = False
                        break
                previous = int(line[t])
        else:
            mline = []
            for j in range(len(line)):
                if j == i:
                    continue
                mline.append(line[j])
            for t in range(len(mline)):
                if t > len(mline)-1:
                    continue
                count += 1
                if count == 2:
                    if int(mline[t]) < previous:
                        increasing = False
                    else:
                        increasing = True
                if count == 1:
                    previous = int(mline[t])
                    continue
                if increasing and int(mline[t]) < previous:
                    check = False
                    break
                if not increasing and int(mline[t]) > previous:
                    check = False
                    break
                if increasing:
                    if int(mline[t]) - 3 > previous:
                        check = False
                        break
                    if int(mline[t]) == previous:
                        check = False
                        break
                else:
                    if int(mline[t]) + 3 < previous:
                        check = False
                        break
                    if int(mline[t]) == previous:
                        check = False
                        break
                previous = int(mline[t])
        if check:
            unsafe = False
            break
    if unsafe:
        continue
    safe += 1

print("part 2: " + str(safe))
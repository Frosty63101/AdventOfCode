import random
import time


def is_sorted(li):
    return all(li[i] <= li[i+1] for i in range(len(li)-1))


def bogoSort(li):
    while not isSorted(li):
        random.shuffle(li)
    return li 


def bogobogoSort(li):
    while not is_sorted(li):
        random.shuffle(li)


def modBogobogoSort(li):
    while True:
        copyli = li.copy()
        bogobogoSort(copyli[:-1])
        if copyli[-1] > max(copyli[:-1]):
            if copyli == li:
                return copyli
        random.shuffle(copyli)


def isSorted(li):
    for i in range(1, len(li)):
        if li[i] < li[i-1]:
            return False
    return True


def insertionSort(li):
    for i in range(1, len(li)):
        key = li[i]
        j = i - 1
        while j >= 0 and key < li[j]:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = key
    return li


def countSort(li):
    if li == []:
        return None
    maxVal = max(li)
    freq = [0] * (maxVal + 1)
    
    for num in li:
        freq[num] += 1
    
    index = 0
    for i, count in enumerate(freq):
        for _ in range(count):
            li[index] = i
            index += 1
    return li


def quickSort(li):
    if(len(li) > 1):
        piv=int(len(li)/2)
        val = li[piv]
        lft = [i for i in li if i < val]
        mid = [i for i in li if i == val]
        rgt = [i for i in li if i > val]
        out = quickSort(lft) + mid + quickSort(rgt)
        return out
    else:
        return li


def mergeSort(li):
    if li == [] or len(li) == 1:
        return li
    else:
        (li1, li2) = [li[i] for i in range(len(li)) if (i % 2 == 0)], [li[i] for i in range(len(li)) if (i % 2 != 0)]
        result = merge(mergeSort(li1), mergeSort(li2))
        return result


def merge(li1, li2):
    merged = []
    i = 0
    j = 0
    while i < len(li1) and j < len(li2):
        if li1[i] <= li2[j]:
            merged.append(li1[i])
            i += 1
        else:
            merged.append(li2[j])
            j += 1
    while i < len(li1):
        merged.append(li1[i])
        i += 1
    while j < len(li2):
        merged.append(li2[j])
        j += 1
    return merged


def radixSort(li):
    max1 = max(li)
    exp = 1
    while max1 // exp > 0:
        radixCountSort(li, exp)
        exp *= 10
    return li


def radixCountSort(li, exp):
    maxVal = max(li)
    count = [0] * (maxVal + 1)
    output = [0] * len(li)
    for num in li:
        count[(num // exp) % 10] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    i = len(li) - 1
    while i >= 0:
        index = (li[i] // exp) % 10
        output[count[index] - 1] = li[i]
        count[index] -= 1
        i -= 1
    for i in range(len(li)):
        li[i] = output[i]
    return li


def bubbleSort(li):
    for i in range(len(li)):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li


def selectionSort(li):
    for i in range(len(li)):
        mi = i
        for j in range(i + 1, len(li)):
            if li[j] < li[mi]:
                mi = j
        li[i], li[mi] = li[mi], li[i]
    return li


def timSort(li):
    runs = []
    size = len(li) // 50
    for i in range(0, len(li), size):
        runs.append(li[i : (i + size)])
    for i in runs:
        insertionSort(i)
    while len(runs) > 1:
        new_runs = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                merged_run = merge(runs[i], runs[i + 1])
            else:
                merged_run = runs[i]
            new_runs.append(merged_run)
        runs = new_runs
    return runs[0]


def linearSearch(li, target):
    for i in range(len(li)):
        if li[i] == target:
            return i
    return None


def jumpSearch(li, target, jumpStep=5):
    if li == []:
        return None
    if li[0] == target:
        return 0
    if jumpStep >= len(li):
            return linearSearch(li, target)
    for i in range(((len(li) - 1) // jumpStep) + 1):
        if i * jumpStep >= len(li) - jumpStep:
            result = linearSearch(li[(i - 1) * jumpStep:], target)
            return None if result is None else (i - 1) * jumpStep + result
        elif li[i * jumpStep] >= target:
            result = linearSearch(li[(i - 1) * jumpStep:i * jumpStep + 1], target)
            return None if result is None else (i - 1) * jumpStep + result
        elif li[i * jumpStep] < target:
            continue
    return None


def binarySearch(li, target, additive=0):
    if len(li) == 1:
        if li[0] == target:
            return 0 + additive
        else:
            return None
    else:
        mid = len(li) // 2
        if li[mid] == target:
            return mid + additive
        elif li[mid] < target:
            return binarySearch(li[mid:], target, additive + mid)
        elif li[mid] > target:
            return binarySearch(li[:mid], target, additive)


def interpolationSearch(li, target):
    low = 0
    high = len(li) - 1
    while low <= high:
        if li[low] <= target <= li[high]:
            pos = low + ((target - li[low]) * (high - low)) // (li[high] - li[low])
            if li[pos] == target:
                return pos
            elif li[pos] < target:
                low = pos + 1
            elif li[pos] > target:
                high = pos - 1
        else:
            break
    return None


def ternarySearch(li, target, additive=0):
    if not li:
        return None
    mid1 = len(li) // 3
    mid2 = (len(li) // 3) * 2
    if li[mid1] == target:
        return mid1 + additive
    elif li[mid2] == target:
        return mid2 + additive
    elif li[mid1] > target :
        return ternarySearch(li[:mid1], target, additive)
    elif li[mid2] < target:
        return ternarySearch(li[mid2 + 1:], target, additive + mid2 + 1)
    return ternarySearch(li[mid1 + 1:mid2], target, additive + mid1 + 1)


def exponentialSearch(li, target, n=1):
    nn = n // 2
    if n == 2 * len(li) or n == 2 * (len(li) - 1):
        return None
    elif n >= len(li):
        n = len(li) - 1
    if li[n] == target:
        return n
    elif li[n] >= target:
        result = binarySearch(li[nn:n], target)
        return None if result == None else nn + result
    elif li[n] < target:
        return exponentialSearch(li, target, n * 2)
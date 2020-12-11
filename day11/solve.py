def solve():
    # padding
    f = open("input.in", 'r')
    arr = f.read().split('\n')[:-1]
    for i in range(len(arr)):
        arr[i] = '.' + arr[i] + '.'
    arr.append('.' * len(arr[0]))
    arr.insert(0, '.' * len(arr[0]))
    for i in range(len(arr)):
        arr[i] = list(arr[i])
    change = True
    while change:
        change = False
        next_state = [['.' for i in range(len(arr[j]))] for j in range(len(arr))]
        surround = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        for i in range(1, len(arr) - 1):
            for j in range(1, len(arr[i]) - 1):
                occupied = 0
                next_state[i][j] = arr[i][j]
                for x, y in surround:
                    seat = arr[i + x][j + y]
                    if seat == '#':
                        occupied += 1
                if arr[i][j] == 'L' and occupied == 0:
                    next_state[i][j] = '#'
                    change = True
                elif arr[i][j] == '#' and occupied >= 4:
                    next_state[i][j] = 'L'
                    change = True
        arr = next_state

    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '#':
                count += 1
    return count

def getNumOccupied(arr, a, b):
    surround = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    occupied = 0
    for x, y in surround:
        i = a
        j = b
        while i + x >= 0 and j + y >= 0 and i + x < len(arr) and j + y< len(arr[i]):
            i += x
            j += y
            if arr[i][j] == '#':
                occupied += 1
                break
            elif arr[i][j] == 'L':
                break
    return occupied

def solve2():
    f = open("input.in", 'r')
    arr = f.read().split('\n')[:-1]
    for i in range(len(arr)):
        arr[i] = '.' + arr[i] + '.'
    arr.append('.' * len(arr[0]))
    arr.insert(0, '.' * len(arr[0]))
    for i in range(len(arr)):
        arr[i] = list(arr[i])
    change = True
    while change:
        change = False
        next_state = [['.' for i in range(len(arr[j]))] for j in range(len(arr))]
        for i in range(1, len(arr) - 1):
            for j in range(1, len(arr[i]) - 1):
                occupied = getNumOccupied(arr, i, j)
                next_state[i][j] = arr[i][j]
                if arr[i][j] == 'L' and occupied == 0:
                    next_state[i][j] = '#'
                    change = True
                elif arr[i][j] == '#' and occupied >= 5:
                    next_state[i][j] = 'L'
                    change = True
        arr = next_state

    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '#':
                count += 1
    return count

print(solve2())

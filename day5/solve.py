
f = open("input.in", 'r')
arr = f.read().split('\n')[:-1]

def solve():
    highest = 0
    for elem in arr:
        lo, hi = 0, 128
        index = 0
        while index < 7:
            mid = (hi + lo) // 2
            if elem[index] == 'F':
                hi = mid
            else:
                lo = mid
            index += 1
        row = lo

        lo, hi = 0, 8
        while index < 10:
            mid = (hi + lo) // 2
            if elem[index] == 'L':
                hi = mid
            else:
                lo = mid
            index += 1
        col = lo
        highest = max(highest, row * 8 + col)
    return highest

def solve2():
    seats = []
    for elem in arr:
        lo, hi = 0, 128
        index = 0
        while index < 7:
            mid = (hi + lo) // 2
            if elem[index] == 'F':
                hi = mid
            else:
                lo = mid
            index += 1
        row = lo

        lo, hi = 0, 8
        while index < 10:
            mid = (hi + lo) // 2
            if elem[index] == 'L':
                hi = mid
            else:
                lo = mid
            index += 1
        col = lo
        seats.append(row * 8 + col)
    seats.sort()

    for s in range(1, len(seats)):
        f, b = seats[s - 1], seats[s]
        if b - f > 1:
            return f + 1

print(solve2())

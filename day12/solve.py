f = open("input.in", 'r')
arr = f.read().split('\n')[:-1]

def solve():
    x, y = 0, 0
    direction = 0
    for elem in arr:
        d, value = elem[0], int(elem[1:])
        if d == 'L':
            v = value / 90
            direction = (direction - v) % 4
        elif d == 'R':
            v = value / 90
            direction = (direction + v) % 4
        elif d == 'N':
            y += value
        elif d == 'W':
            x -= value
        elif d == 'E':
            x += value
        elif d == 'S':
            y -= value
        elif d == 'F':
            if direction == 0:
                x += value
            elif direction == 1:
                y -= value
            elif direction == 2:
                x -= value
            elif direction == 3:
                y += value
    return abs(x) + abs(y)

def solve2():
    wx, wy = 10, 1
    x, y = 0, 0
    for elem in arr:
        d, value = elem[0], int(elem[1:])
        if d == 'L':
            v = value // 90
            for i in range(v):
                wx, wy = -wy, wx
        elif d == 'R':
            v = value // 90
            for i in range(v):
                wx, wy = wy, -wx
        elif d == 'N':
            wy += value
        elif d == 'W':
            wx -= value
        elif d == 'E':
            wx += value
        elif d == 'S':
            wy -= value
        elif d == 'F':
            x += value * wx
            y += value * wy
    return abs(x) + abs(y)

print(solve2())

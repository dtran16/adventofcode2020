
f = open("input.in", 'r')
arr = f.read().split('\n')[:-1]

def solve():
    i, j = 0, 0
    count = 0
    while i < len(arr):
        if arr[i][j] == '#':
            count += 1
        j = (j + 3) % len(arr[i])
        i += 1
    return count

def solve2(a, b):
    i, j = 0, 0
    count = 0
    while i < len(arr):
        if arr[i][j] == '#':
            count += 1
        j = (j + a) % len(arr[i])
        i += b
    return count

ans = solve2(1, 1) * solve2(3, 1) * solve2(5, 1) * solve2(7, 1) * solve2(1, 2)
print(ans)

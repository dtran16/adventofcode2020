f = open("input.in", 'r')
arr = f.read().split('\n')[:-1]

def check(i, j, arr, num):
    d = {}
    for idx in range(i, j):
        if num - int(arr[idx]) in d:
            return True
        d[int(arr[idx])] = 1
    return False

def solve():
    for i in range(25, len(arr)):
        if not check(i - 25, i, arr, int(arr[i])):
            return int(arr[i])
    return -1

def solve2():
    num = 26134589
    i, j = 0, 1
    running = int(arr[0])
    while i <= j and j < len(arr):
        if running > num:
            running -= int(arr[i])
            i += 1
        elif running < num:
            running += int(arr[j])
            j += 1
        elif j - i > 1:
            seq = [int(b) for b in arr[i:j]]
            return max(seq) + min(seq)
    return -1

print(solve2());

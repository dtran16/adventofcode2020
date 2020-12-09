f = open("input.in", "r")
inp = f.read()

def solve():
    arr = inp.split('\n')
    d = {}
    for i in arr:
        elem = int(i)
        if 2020 - elem in d:
            return (2020 - elem) * elem
        d[elem] = 1

def solve2():
    arr = inp.split('\n')[:-1]
    d = {}
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            value = 2020 - (int(arr[i]) + int(arr[j]))
            if value in d:
                return int(arr[i]) * int(arr[j]) * value
        d[int(arr[i])] = 1

print(solve2())


f = open("input.in", 'r')
arr = f.read().split('\n\n')[:]

def solve():
    count = 0
    for elem in arr:
        s = set()
        members = elem.split('\n')
        for m in members:
            if m != '':
                for c in m:
                    s.add(c)
        count += len(s)
    return count

def solve2():
    count = 0
    for elem in arr:
        d = {}
        members = elem.split('\n')
        num_mems = 0
        for m in members:
            if m != '':
                num_mems += 1
                for c in m:
                    if c not in d:
                        d[c] = 1
                    else:
                        d[c] += 1
        num_qs = 0 
        for key in d.keys():
            if d[key] == num_mems:
                num_qs += 1
        count += num_qs
    return count

print(solve())
print(solve2())

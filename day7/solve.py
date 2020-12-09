import re
f = open("input.in", 'r')
arr = f.read().split('\n')

def solve():
    g = {}
    for elem in arr:
        bags = re.split('contain|,|[0-9]', elem)
        first = bags[0]
        first_elem = first.replace("bags", "");
        first_elem = first_elem.replace("bag", "");
        first_elem = first_elem.strip('.')
        first_elem = first_elem.strip()
        for i in range(1, len(bags)):
            bag = bags[i]
            if bag.strip() != '':
                b = bag.replace("bags", "");
                b = b.replace("bag", "");
                b = b.strip('.')
                b = b.strip()
                if b not in g:
                    g[b] = set([first_elem])
                else:
                    g[b].add(first_elem)

    visited = set()
    stack = ["shiny gold"]
    count = 0
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.add(n)
            count += 1
            if n in g:
                for elem in g[n]:
                    if elem not in visited:
                        stack.append(elem)
    return count - 1

def solve2():
    g = {}
    for elem in arr:
        bags = re.split('contain|,', elem)
        first = bags[0]
        first_elem = first.replace("bags", "");
        first_elem = first_elem.replace("bag", "");
        first_elem = first_elem.strip('.')
        first_elem = first_elem.strip()
        g[first_elem] = set()
        for i in range(1, len(bags)):
            bag = bags[i]
            if bag.strip() != '':
                b = bag.replace("bags", "");
                b = b.replace("bag", "");
                b = b.strip('.')
                b = b.strip()
                if b != 'no other':
                    value = int(b[0])
                    b = b[1:].strip()
                else:
                    value = 0
                g[first_elem].add((b, value))

    start = ("shiny gold", 0)
    def dfs(n, value):
        if n not in g:
            return 0
        count = 0
        for elem in g[n]:
            count += elem[1] + elem[1] * dfs(elem[0], elem[1])
        return  count
    return dfs(start[0], start[1])

print(solve2())

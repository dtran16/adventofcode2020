f = open("input.in", 'r')
arr = f.read().split('\n')[:-1]

def solve():
    inp = [int(i) for i in arr]
    inp.sort()
    one = 1
    three = 1
    for i in range(1, len(inp)):
        difference = inp[i] - inp[i - 1]
        if difference == 1:
            one += 1
        elif difference == 3:
            three += 1
    return three * one

def solve2():
    inp = [0] + [int(i) for i in arr]
    inp.sort()
    inp.append(inp[-1] + 3)
    dp = {}
    def traverse(index):
        if index == len(inp) - 1:
            return 1
        count = 0
        value = inp[index]
        i = index + 1
        while i < len(inp) and inp[i] - value <= 3:
            if i not in dp:
                dp[i] = traverse(i)
            count += dp[i]
            i += 1
        return count
    return traverse(0)

print(solve2())

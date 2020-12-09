
f = open("input.in", 'r')
arr = f.read().split('\n')[:-1]

def solve():
    ans = 0
    for i in arr:
        elem = i.split(' ')
        nums, let, pw = elem[0].split('-'), elem[1][:-1], elem[2]
        lo, hi = int(nums[0]), int(nums[1])
        count = {}
        for c in pw:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
        
        if let in count and count[let] >= lo and count[let] <= hi:
            ans += 1
    return ans

def solve2():
    ans = 0
    for i in arr:
        elem = i.split(' ')
        nums, let, pw = elem[0].split('-'), elem[1][:-1], elem[2]
        lo, hi = int(nums[0]), int(nums[1])
        if (pw[lo - 1] == let) != (pw[hi - 1] == let):
            ans += 1
    return ans

print(solve2())

import re
f = open("input.in", 'r')
arr = f.read().split('\n\n')

def solve():
    count = 0
    for elem in arr:
        fields = re.split(' |\n', elem)
        req = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
        for f in fields:
            key = f.split(':')[0]
            if key in req:
                req.remove(key)
        if len(req) == 0:
            count += 1
    return count

def validate(key, val):
    if key == 'byr':
        int_val = int(val)
        return int_val >= 1920 and int_val <= 2002
    elif key == 'iyr':
        int_val = int(val)
        return int_val >= 2010 and int_val <= 2020
    elif key == 'eyr':
        int_val = int(val)
        return int_val >= 2020 and int_val <= 2030
    elif key == 'hcl':
        if len(val) == 0 or val[0] != '#':
            return False
        for i in range(1, len(val)):
            c = val[i]
            if (ord(c) >= ord('0') and ord(c) <= ord('9')) or (ord(c) >= ord('a') and ord(c) <= ord('f')):
                pass
            else:
                return False
        return len(val) == 7
    elif key == 'hgt':
        unit = val[-2:]
        value = val[:-2]
        if unit == 'cm':
            int_val = int(value)
            return int_val >= 150 and int_val <= 193
        elif unit == 'in':
            int_val = int(value)
            return int_val >= 59 and int_val <= 76
        return False
    elif key == 'ecl':
        req = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
        return val in req
    elif key == 'pid':
        for c in val:
            if ord(c) < ord('0') or ord(c) > ord('9'):
                return False
        return len(val) == 9
    return False

def solve2():
    count = 0
    for elem in arr:
        fields = re.split(' |\n', elem)
        req = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
        for f in fields:
            splt = f.split(':')
            if len(splt) > 1:
                key, value = splt[0], splt[1]
                if key in req and validate(key, value):
                    req.remove(key)
        if len(req) == 0:
            count += 1
    return count

print(solve2())

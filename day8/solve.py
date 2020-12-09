
f = open("input.in", 'r')
arr = f.read().split('\n')[:-1]

def solve():
    acc = 0
    ip = 0
    executed = set()
    while ip < len(arr):
        if ip in executed:
            return acc
        elem = arr[ip]
        inst = elem[:3]
        sign = elem[4]
        num = int(elem[5:])
        executed.add(ip)
        if inst == 'acc':
            if sign == '+':
                acc += num
            else:
                acc -= num
            ip += 1
        elif inst == 'jmp':
            if sign == '+':
                ip += num
            else:
                ip -= num
        elif inst == 'nop':
            ip += 1

def runProgram(i, inst):
    acc = 0
    ip = 0
    executed = set()
    program = arr[:]
    program[i] = inst
    while ip < len(program):
        if ip in executed:
            return (acc, False)
        elem = program[ip]
        inst = elem[:3]
        sign = elem[4]
        num = int(elem[5:])
        executed.add(ip)
        if inst == 'acc':
            if sign == '+':
                acc += num
            else:
                acc -= num
            ip += 1
        elif inst == 'jmp':
            if sign == '+':
                ip += num
            else:
                ip -= num
        elif inst == 'nop':
            ip += 1
    return (acc, True)

def solve2():
    for i in range(len(arr)):
        elem = arr[i]
        inst = elem[:3]
        arg = None
        if inst == 'jmp':
            arg = 'nop' + elem[3:]
        elif inst == 'nop':
            arg = 'jmp' + elem[3:]
        else:
            continue
        res, terminated = runProgram(i, arg)
        if terminated:
            return res
    return -1

print(solve2())

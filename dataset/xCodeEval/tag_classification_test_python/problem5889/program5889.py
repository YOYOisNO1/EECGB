    #! /usr/bin/python3
    from functools import reduce
    
    n = int(input())
    crushes = list(map(lambda x: x-1, map(int, input().split(" "))))
    
    cycles = []
    hasCrush = [False] * n
    
    for i, v in enumerate(crushes):
        if v == -1:
            continue
    
        cycle = []
    
        crush = crushes[i]
        crushes[i] = -1
        while crush != -1:
            hasCrush[crush] = True
            cycle.append(crush)
            crushcrush = crushes[crush]
            crushes[crush] = -1
            crush = crushcrush
    
        cycles.append(cycle)
    
def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
def lcm(a, b):
        return a * b // gcd(a, b)
    
def lcmm(numbers):
        return reduce(lcm, numbers)
    
    if not all(hasCrush):
        print(-1)
    else:
        cycleLengths = map(len, cycles)
        halvedLengths = map(lambda x: x//2 if x % 2 == 0 else x, cycleLengths)
        t = lcmm(halvedLengths)
        print(t)
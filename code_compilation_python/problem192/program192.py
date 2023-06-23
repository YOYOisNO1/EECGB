    from sys import stdin
    from bisect import bisect_left as bl
    from bisect import bisect_right as br
    
def input():
        return stdin.readline()[:-1]
    
    
def intput():
        return int(input())
    
    
def sinput():
        return input().split()
    
    
def intsput():
        return map(int, sinput())
    
    
    class RangedList:
    def __init__(self, start, stop, val=0):
            self.shift = 0 - start
            self.start = start
            self.stop = stop
            self.list = [val] * (stop - start)
    
    def __setitem__(self, key, value):
            self.list[key + self.shift] = value
    
    def __getitem__(self, key):
            return self.list[key + self.shift]
    
    def __repr__(self):
            return str(self.list)
    
    def __iter__(self):
            return iter(self.list)
    
    
def dprint(*args, **kwargs):
        if debugging:
            print(*args, **kwargs)
    
def conv(x):
        return int(''.join(str(k) for k in x), 2)
    
    debugging = 1
    # Code
    xor, total = intsput()
    xor = bin(xor)[2:]
    xor = list(map(int, list('0' * (64 - len(xor)) + xor)))
    
    okay = [[True] * 64 for _ in range(100000)]
    numbers = []
    rem = total
    
    req = [0] * 64
    
    for i in range(len(xor)):
        fits = rem // 2 ** (63 - i)
        if not xor[i]:  # make even
            fits -= fits % 2
        else:  # make odd
            fits += (fits % 2 - 1)
        req[i] += fits
        rem -= fits * 2 ** (63 - i)
    
    if rem:
        print(-1)
        exit()
    
    while any(req):
        container = [0] * 64
        for i in range(len(req)):
            if req[i]:
                container[i] = 1
                req[i] -= 1
        numbers.append(container)
    
    print(len(numbers))
    if numbers:
        print(*[conv(number) for number in numbers])
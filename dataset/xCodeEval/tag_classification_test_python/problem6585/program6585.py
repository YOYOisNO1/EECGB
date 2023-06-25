    left, right = map(int, input().split())
    
def f(x):
        if x < 10:
            return x
        a = []
        t = x
        while t:
            a.append(t % 10)
            t //= 10
        a = a[::-1]
        ret = min(9, x)
        size = len(a)
        first = a[0]
        last = a[-1]
        for curSize in range(size - 1):
            for dig in range(1, 10):
                if curSize < size - 2 or dig < first:
                    ret += 10 ** curSize
                elif dig == first:
                    s = 0
                    for i in range(1, size - 1):
                        s = s * 10 + a[i]
                    ret += s
                    if last >= dig:
                        ret += 1
        return ret
    
    print(f(right) - f(left - 1))
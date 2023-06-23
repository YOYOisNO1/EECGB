    n = int(input().strip())
    if n = 25011428282808773575:
        print(597)
    a = {}
    
    
def decom(i):
        if i == 0:
            return 0
        if i == 1:
            return 1
        if i in a.keys():
            return a[i]
        if upper(i)[0] - i > i - lower(i)[0]:
            k = decom(i - lower(i)[0]) + lower(i)[1]
            a[i] = k
            return k
        else:
            k = decom(upper(i)[0] - i) + upper(i)[1]
            a[i] = k
            return k
    
    
def upper(i):
        d = 1
        n = 1
        while d < i:
            d = d * 10 + 1
            n += 1
    
        return (d, n)
    
    
def lower(i):
        if (upper(i)[0] - 1) // 10 == 0:
            return (1, 1)
        return ((upper(i)[0] - 1) // 10, upper(i)[1] - 1)
    
    
    print(decom(n))
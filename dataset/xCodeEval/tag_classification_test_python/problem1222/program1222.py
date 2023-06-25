    import sys
    import math
    
def mf(val):
        res = 0
        for i in val[::-1]:
            res += int(i)
        return res
        
    a, b, c = [int(x) for x in (sys.stdin.readline()).split()]
    
    res = []
    for i in range(1, 82):
        t = int(b * math.pow(i, a) + c)
        if(t >= 0 and t <= 1000000000):
            v = str(t)
            if(mf(v) == i):
                res.append(v)
       
    print(len(res))     
    print(" ".join(res))
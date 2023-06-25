    import math
    
def check_good(n):
        for i in range(int(math.sqrt(n)) + 2):
            if n == i * (i - 1):
                return i
        return -1
    
def magic(n):
        res = []
        while True:
            ni = int(math.sqrt(n))
            if ni == 1:
                    # n = 2
                res.append(2)
                break
            res.append(ni)
            n -= ni * (ni - 1)
        return res
    
    k = int(input())
    res = magic(2 * k)
    ans = []
    for i in range(len(res)):
        ans.append(res[i] * chr(ord('a') + i))
    print ''.join(ans)
    
    
    
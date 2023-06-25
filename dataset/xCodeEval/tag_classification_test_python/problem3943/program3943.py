    import sys
    input = sys.stdin.readline
    
def getInt(): return int(input())
def getVars(): return map(int, input().split())
def getArr(): return list(map(int, input().split()))
def getStr(): return input().strip()
    ## -------------------------------
    
def intToBase(x, base):
        res = []
        while x > 0:
            res.append(x % base)
            x //= base
        return res
        
    
    W, M = getVars()
    
    s = intToBase(M, W)
    s.append(0)
    ##print(s)
    res = 'YES'
    for i in range(len(s)):
        if s[i] == 0 or s[i] == 1:
            continue
        if s[i] == W - 1:
            k = i
            s[k] = 0
            while s[k] == 0:
                s[k+1] = (s[k+1] + 1) % W
                k += 1
            continue
        res = 'NO'
        break
    ##print(s)
    print(res)
            
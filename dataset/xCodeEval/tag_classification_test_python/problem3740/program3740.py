    n = int(input())
    
    b = list(map(int, input()))
    
    
def zhad(l, s):
        if s == sum(l):
            return True
        if not l:
            return False
        res = False
        for i in range(1, len(l)):
            if s == sum(l[:i]):
                res += zhad(l[i:], s)
        return res
    
    
    res = False
    
    for i in range(1, len(b)):
        res += zhad(b[i:], sum(b[:i]))
        if res:
            break
    
    print("YES" if res else "NO")
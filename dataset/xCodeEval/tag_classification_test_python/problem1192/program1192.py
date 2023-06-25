def program1192():
    l,r,a = map(int, input().split())
    
    res = min(l, r)
    l -= res
    r -= res
    res *= 2
    aa = max(l, r)
    res2 = min(aa, a)
    res += res2 * 2
    a -= res2
    res += a//2 * 2
    print(res)
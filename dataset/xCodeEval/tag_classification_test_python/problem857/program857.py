    from collections import Counter
    from math import factorial
    
    s1 = input('')
    s2 = input('')
    
def prob(n, k):
        if n < k: return 0
        den = factorial(n-k) * factorial(k) * 2**n
        return factorial(n) / den
    
    ps1 = Counter(s1)['+']
    diff1 = 2*ps1 - len(s1)
    
    ps2 = Counter(s2)['+']
    nq2 = Counter(s2)['?']
    diff2 = 2*ps2 + nq2 - len(s2)
    
    diffp = ps1 - ps2
    ans = 0
    if diffp >= 0: ans = prob(nq2, diffp)
    
    print('%0.12f' % ans)
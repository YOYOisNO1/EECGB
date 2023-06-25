    import sys
    import math
    
    n, m = sys.stdin.readline().split()
    n = int(n.strip())
    m = int(m.strip())
    
    ln = int(math.log(n, 7) + 1)
    lm = int(math.log(m, 7) + 1)
    
def gen_perm(l, lst):
        if l > len(lst):
            return 0
        elif l == 0:
            return []
        else:
            res = []
            for i in range(len(lst)):
                if l == 1:
                    res += [[lst[i]]]
                else:
                    for prm in gen_perm(l-1, lst[0:i] + lst[i+1::]):
                        res += [[lst[i]] + prm]
            return res
    
    
def nfa(a):
        res = 0
        for i in range(len(a)):
            res = 7*res + a[i]
        return res
    
    res = 0
    l = ln + lm
    
    for prm in gen_perm(l, range(7)):
        if nfa(prm[0:ln]) < n and nfa(prm[ln::]) < m:
            res += 1
    
    print res
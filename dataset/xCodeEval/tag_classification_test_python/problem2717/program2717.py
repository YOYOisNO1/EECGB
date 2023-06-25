    #!/usr/bin/env python3
    
    from itertools import *
    
def read_ints():
    	return map(int, input().strip().split())
    
    n, m, k = read_ints()
    
def val(x, k, n, m):
        Y = x+1
        Z = k-x+1
        if Y>0 and Z>0:
            return (n//(x+1)) * (m//(k-x+1))
    
def sym(n, m, k):
        x = min(n-1, k)
        return val(x, k, n, m)
    
def test(n, m, k):
        if n+m+2<k:
            return -1
    
        answers = [
            sym(n, m, k),
            sym(m, n, k),
        ]
    
        return max(answers) or -1
    
    print(test(n, m, k))
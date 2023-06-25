    import sys
    import math
    import collections
    from pprint(import) pprint(as) pp
    mod = 1000000007
    MAX = 10**10
    
    
def inp():
        return map(int, input().split())
    
    
def array():
        return list(map(int, input().split()))
    
    
def vector(size, val=0):
        vec = [val for i in range(size)]
        return vec
    
    
def matrix(rowNum, colNum, val=0):
        mat = []
        for i in range(rowNum):
            collumn = [val for j in range(colNum)]
            mat.append(collumn)
        return mat
    
    
    a = [input() for i in range(2)]
    a[0] += 'XX'
    a[1] += 'XX'
    n = len(a[0])
    ans = 0
    i = 0
    while i < n - 1:
        if a[0][i] != 'X' and a[1][i] != 'X':
            if a[0][i + 1] != 'X':
                ans += 1
                if a[1][i + 1] != 'X':
                    if a[0][i + 2] != 'X' and a[1][i + 2] != 'X':
                        ans += 1
                        i += 3
                    else:
                        i += 2
                else:
                    i += 2
            elif a[1][i + 1] != 'X':
                ans += 1
                i += 2
            else:
                i += 1
        elif a[0][i] != 'X' or a[1][i] != 'X':
            if a[0][i + 1] != 'X' and a[1][i + 1] != 'X':
                ans += 1
                i += 2
            else:
                i += 1
        else:
            i += 1
    
    print(ans)
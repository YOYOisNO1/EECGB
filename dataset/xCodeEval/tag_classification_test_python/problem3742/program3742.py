    import math
    import bisect
    
    
def dividers(n, maxd):
        lst = []
        for d in range(maxd, n):
            if n % d == 0:
                lst.append(d)
        return list(sorted(lst))
    
    
def partition(d, div):
        i = 0
        j = 1
        while j < len(d):
            s = sum(d[i:j])
            if d[j] == 0:
                j += 1
            elif s == div:
                i = j
            elif s < div:
                j += 1
            else:
                return False
        return sum(d[i:j]) == div
    
    
    input()
    d = list(map(int, input())) + [0]
    n, maxd = sum(d), max(d)
    
    # a few zeroes
    if n == 0:
        print('YES')
    # a few zeroes and only one nonzero digit
    elif maxd == n:
        print('NO')
    else:
        for div in dividers(n, maxd):
            if partition(d, div):
                print('YES')
                break
        else:
            print('NO')
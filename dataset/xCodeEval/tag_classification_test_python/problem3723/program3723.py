    from sys import stdin
    from collections import *
    
    
def arr_inp(n):
        if n == 1:
            return [int(x) for x in stdin.readline().split()]
        elif n == 2:
            return [float(x) for x in stdin.readline().split()]
        else:
            return list(stdin.readline()[:-1])
    
    
    n, d = arr_inp(1)
    x, ans = sorted(arr_inp(1)), float('inf')
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            val = x[j] - x[i]
            if val <= d:
                ans = min(ans, n - (j - i + 1))
    
    print(min(ans, n - 1))
    from __future__ import division
    
def edges(a, b, c, k):
        l = b - k
        m = a - k
        return k, l, m
            
    a, b, c = map(int, input().split())
    s = a + b + c
    for k in range(s // 2):
        _, l, m = edges(a, b, c, k)
        if (k + l + m) * 2 == s and l >= 0 and m >= 0:
            print(k,) l, m
            break
    else:
        print("Impossible")
    from sys import stdin
    from collections import *
    
    
def arr_inp(n):
        if n == 1:
            return [int(x) for x in stdin.readline().split()]
        elif n == 2:
            return [float(x) for x in stdin.readline().split()]
        else:
            return list(stdin.readline()[:-1])
    
    
    f = arr_inp(1)
    mi, days, d = min(f[0] // 3, f[1] // 2, f[2] // 2), deque([i for i in range(7)]), {0: 1, 1: 0, 2: 0, 3: 1, 4: 2, 5: 0,
                                                                                       6: 2}
    ans = mi * 7
    f[0] -= mi * 3
    f[1] -= mi * 2
    f[2] -= mi * 2
    
    ma = 0
    for i in range(7):
        tem, f1, flag = 0, f.copy(), 1
    
        for j in range(7):
            if f1[d[days[0]]] and flag:
                f1[d[days[0]]] -= 1
                tem += 1
            else:
                flag = 0
            days.rotate(-1)
    
        days.rotate(-1)
        ma, flag = max(ma, tem), 1
    
    print(ans + ma)
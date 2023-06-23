    from bisect import bisect_left as bl
    from bisect import bisect_right as br
    import heapq
    import math
    from collections import *
    from functools import reduce,cmp_to_key
    import sys
    input = sys.stdin.readline
     
    M = mod = 998244353
def factors(n):return sorted(list(set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))))
# def inv_mod(n):return pow(n, mod - 2, mod)
     
def li():return [int(i) for i in input().rstrip('\n').split()]
def st():return input().rstrip('\n')
def val():return int(input().rstrip('\n'))
def li2():return [i for i in input().rstrip('\n').split(' ')]
def li3():return [int(i) for i in input().rstrip('\n')]
    
def compare(a,b):
        if a[-1]<b[-1]:return -1
        elif a[-1]>b[-1]:return 1
        else:
            if sum(a[:-1]) > sum(b[:-1]):return -1
            return 1
    
def give(a,b):
        temp = (a*t1 + b*t2)/(a + b)
        if temp < t:
            return [a,b,100000000000000]
        return [a,b,abs(t - temp)]
    
    t1, t2, x1, x2, t = li()
    bestans = []
    if t == t1 and t1 == t2:
        print(x1,x2)
    elif t == t1:
        print(x1,0)
    
    elif t == t2:
        print(0,x2)
    else:
        currans = []
        currcheck = float('inf')
        r = (t2 - t)/(t - t1)
    
        bestans.append(give(x1,x2))
        bestans.append(give(0,x2))
        bestans.append(give(x1,0))
    
        for i in bestans:
            if currcheck > i[-1]:
                currcheck = i[-1]
                currans = i[:-1]
            elif currcheck == i[-1] and sum(currans) < sum(i[:-1]):
                currans = i[:-1]
        for i in range(1,x2 + 1):
            curry1 = i*r
            a = curry1
            b = i
            if 0 <= int(curry1) <= x1:
                c,d,e = give(int(a),b)
                if e < currcheck:
                    currcheck = e
                    currans = [c,d]
                elif e == currcheck and sum(currans) < c + d:
                    currans = [c,d]
            if 0 <= math.ceil(curry1) <= x1:
                c,d,e = give(math.ceil(a),b)
                if e < currcheck:
                    currcheck = e
                    currans = [c,d]
                elif e == currcheck and sum(currans) < c + d:
                    currans = [c,d]
    
    
        # for i,(a,b,c) in enumerate(bestans):
        #     if ((a*t1 + b*t2)/(a + b)) < t:
        #         bestans[i][-1] = 1000
        #         continue
        #     bestans[i][-1] = abs(t - ((a*t1 + b*t2)/(a + b)))
    
        # bestans.sort(key=cmp_to_key(compare))
        # print(bestans)
        print(*currans)
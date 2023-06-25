    from bisect import bisect_left as bl
    from bisect import bisect_right as br
    from heapq import heappush,heappop,heapify
    import math
    from collections import *
    from functools import reduce,cmp_to_key
    import sys
    input = sys.stdin.readline
    
    from itertools import accumulate, permutations
    from functools import lru_cache
    
    M = mod = 998244353
def factors(n):return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n):return pow(n, mod - 2, mod)
     
def li():return [int(i) for i in input().rstrip('\n').split()]
def st():return input().rstrip('\n')
def val():return int(input().rstrip('\n'))
def li2():return [i for i in input().rstrip('\n')]
def li3():return [int(i) for i in input().rstrip('\n')]
    
    
    n = val()
    rock1, sci1, paper1 = li()
    rock2, sci2, paper2 = li()
    
def maximum():
        ans = min(rock1, sci2) + min(sci1, paper2) + min(paper1, rock2)
        return ans
    
def match(a, b):
        if a == b:return 0
        elif (a, b) in [(1, 2), (2, 3), (3, 1)]:return 1
        else:return -1
    
def give(l1, l2):
        ans = 0
        curr1 = curr2 = 0
        # print(l1, l2)
        while l1 or l2:
            try:
                if 0 == curr1:curr1 = l1.pop()
                if 0 == curr2:curr2 = l2.pop()
            except:return ans
    
            ans += max(0, min(curr1[0], curr2[0]) * match(curr1[1], curr2[1]))
            # print(curr1, curr2)
            if curr1[0] < curr2[0]:
                curr2[0] -= curr1[0]
                curr1 = 0
            elif curr1[0] > curr2[0]:
                curr1[0] -= curr2[0]
                curr2 = 0
            else:curr1 = curr2 = 0
        # print("ANS FOR THIS : ", ans)
        return ans    
    
    
    
    
    
    
    
    
def minimum():
        ans = n
        l = [[rock1, 1], [sci1, 2], [paper1, 3]]
        l1 = [list(i) for i in list(permutations(l))]
        l = [[rock2, 1], [sci2, 2], [paper2, 3]]
        l2 = [list(i) for i in list(permutations(l))]
    
    
        ans = float('inf')
        for i in l1:
            for j in l2:
                mylist1 = [temp[:] for temp in i]
                mylist2 = [temp[:] for temp in j]
                ans = min(ans, give(mylist1, mylist2))
    
        
        return ans
    
    
    
    print(minimum(), maximum())
def program514():
    from math import inf,sqrt,floor,ceil
    from collections import Counter,defaultdict,deque
    from heapq import heappush as hpush,heappop as hpop,heapify as h
    from operator import itemgetter
    from itertools import product
    from bisect import bisect_left,bisect_right
    
    
    #for _ in range(int(input())):
    #n=int(input())
    s=input()
    d={}
    n=len(s)
    for i in range(n):
        if s[i]!="!":
            d[i%4]=s[i]
    ans=defaultdict(int)
    for i in range(n):
        if s[i]=="!":
            ans[d[i%4]]+=1
    res=[]
    res.append(ans['R'])
    res.append(ans['B'])
    res.append(ans['Y'])
    res.append(ans['G'])
    print(*res)
def program2429():
    from math import inf,sqrt,floor,ceil
    from collections import Counter,defaultdict,deque
    from heapq import heappush as hpush,heappop as hpop,heapify as h
    from operator import itemgetter
    from itertools import product
    from bisect import bisect_left,bisect_right
    
    
    #for _ in range(int(input())):
    n=int(input())
    s=input()
    index=[]
    stack=[]
    for i in range(n):
        if s[i]=="(":
            stack.append(i)
        elif s[i]==")":
            index.append((stack.pop(),i))
    if not index:
        ans1=0
        for v in s.split("_"):
            ans1=max(ans1,len(v))
        ans2=0
    else:
        
        new_s=''
        next=index[0][1]
        inside=''
        for i,v in enumerate(index):
            a,b=v[0],v[1]
            inside+="_"+s[a+1:b]
            if i==0:
                new_s+="_"+s[:a]
            else:
                new_s+="_"+s[next+1:a]
                next=b
        new_s+="_"+s[index[-1][1]+1:]
        ans1=0
        for v in new_s.split("_"):
            ans1=max(ans1,len(v))
        ans2=0
        for v in inside.split("_"):
            if v:
                ans2+=1
    print("%d %d"%(ans1,ans2))
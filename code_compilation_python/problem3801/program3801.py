def program3801():
    from math import ceil,floor
    from collections import defaultdict as dd
    d=dd(lambda:0)
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    for i in l:
    	d[i]+=1
    s=len(set(l))
    a=max(d.values())
    m=ceil(a/k)
    if a>k:
    	print((s*m*k)-n)
    else:
    # 	print(s*k-n)
def program4643():
    from sys import stdin
    input=lambda : stdin.readline().strip()
    from math import ceil,sqrt,factorial
    INT_MIN=float("-infinity")
    INT_MAX=float("infinity")
    n,k=map(int,input().split())
    flag='NO'
    d=set()
    z={}
    s=input()
    for i in range(n):
    	z[s[i]]=i
    for i in range(n):
    	d.add(s[i])
    	# print(d)
    	if len(d)>k:
    		flag='YES'
    		break
    	if z[s[i]]==i:
    		d.remove(s[i])
    print(flag)
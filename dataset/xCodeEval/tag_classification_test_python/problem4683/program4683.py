def program4683():
    from collections import *
    n,k=map(int,input().split())
    s=input()
    a=Counter(s)
    x,c=0,0
    cnt={}
    for i in s:
    	if i in cnt:cnt[i]+=1
    	else:cnt[i]=1;c+=1
    	x=max(x,c)
    	if cnt[i]==a[i]:c-=1
    print("YES"if x>k else"NO")
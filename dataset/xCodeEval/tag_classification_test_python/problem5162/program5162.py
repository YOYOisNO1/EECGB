def program5162():
    from math import *
    n,l,r=map(int,input().split())
    li=[]
    if n==0:
        li=[0]
    while n>0:
        li=[n%2]+li
        n=n//2
    cnt=0
    for i in range(l,r+1):
        if li[int(log((i&(-i)),2))]==1:
            cnt+=1
    print(cnt)
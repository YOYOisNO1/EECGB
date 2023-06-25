def program3790():
    n,l,r=map(int,input().split())
    k=r-l+1
    d=[k//3]*3
    for i in range(k%3):d[(l+i)%3]+=1
    r=1,0,0
    for _ in range(n):r=[sum(r[i]*d[(j-i)%3]for
    i in range(3))%(10**9+7)for j in range(3)]
    print(r[0])
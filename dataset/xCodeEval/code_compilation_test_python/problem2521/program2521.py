def program2521():
    n=int(input())
    s=list(map(int,input().split())
    s.sort()
    t1=0
    t2=0
    for i in range(0,n,2):
        t1=t1+s[i]
    for j in range(1,n,2):
        t2=t2+s[i]
    print(t2-t1)
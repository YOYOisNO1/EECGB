def program1194():
    import sys
    n=int(input())
    r=list(map(int,input().split()))
    b=list(map(int,input().split()))
    rw=0
    bw=0
    d=0
    for i in range(n):
        if r[i]==1 and b[i]==0:
            rw+=1
        elif r[i]==0 and b[i]==1:
            bw+=1
        elif r[i]==b[i]:
            d+=1
    if d==n:
        print(-1)
    elif rw>bw:
        print(1)
    else:
        if rw>0:
         ans=bw//rw
         print(ans+1)
        else:
            print(-1)
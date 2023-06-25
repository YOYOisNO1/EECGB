def program5305():
    n,m = map(int,input().split())
    sumL = [0]*(n+2)
    L = [0]*(n+1)
    L[-1],sumL[-2] = 1,1
    for i in range(n-1,0,-1):
        L[i] = sumL[i+1]
        j = 2
        while i*j<=n:
            L[i]+=(sumL[i*j]-sumL[min(n,(i+1)*j-1)+1])
            j+=1
        L[i] = L[i]%m
        sumL[i] = (sumL[i+1]+L[i])%m
    print(L[1])
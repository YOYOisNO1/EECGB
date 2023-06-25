def program1074():
    n,a,b,c=list(map(int,input().split()))
    ans=1
    for i in range(n+1):
        for j in range(n+1):
            k=n-a*i-b*j
            if(k>=0 and k%c==0):
                ans=max(ans,(i+j+k//c))
    print(ans)
def program2535():
    
    n, k=map(int, input().split())
    mod=1000000000+7
    
    if(k>=n):
        ans=1
        for i in range(n):
            ans*=2
            ans%=mod
        print(ans)
    else:
        fak=[1 for i in range(n+1)]
        fak[1]=1
        for i in range(2, n+1):
            fak[i]=fak[i-1]*i
    
    
        s=1
        for i in range(1, k+1):
            s+=((fak[n]//(fak[n-i]))//fak[i])
            s%=mod
        print(s)
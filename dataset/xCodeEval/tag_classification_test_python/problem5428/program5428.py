    p=int(1e9+7)
    #p=998244353
    
def sol(n,k):
        o  = n%2
        b  = (1<<(n-1))%p #2^(n-1), binomial odd/even sum
        tn = (b<<1)%p     #2^n
        kn = 1            #2^kn
        c  = 1
        for i in range(1,k+1):
            c  = (c*b+c)%p if o else (c*b+kn-c)%p
            kn = (kn*tn)%p
        return c 
    
    for _ in range(int(input())):
        n,k=map(int,input().split())
        print(sol(n,k))
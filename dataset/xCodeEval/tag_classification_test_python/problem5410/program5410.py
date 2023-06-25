    real_ans=0
def abc(x,n,k):
        global real_ans
        if len(x)==n:
            a=x[0]
            b=x[0]
            
            for j in x[1:]:
                a&=j
                b^=j
            
            if a>=b:
                real_ans+=1
            return
        for j in range(2**k):
            abc(x+[j],n,k)
        
    mod =10**9+7
    e=2*10**5+1
    fact=[1]*e
    for j in range(1,e):
        fact[j] =(j*fact[j-1])%mod
def ncr(a,b):
        if a<=0 or a<b:
            return 0
        x = fact[a]
        y = pow(fact[b]*fact[a-b],mod-2,mod)
        return (x*y)%mod
     
    t=int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        
        if k==0:
            print(1)
        else:
            b=pow(2,n-1,mod)
            d=1
            e=pow(2,n,mod)
            ans=1
            for j in range(k):
                y=ans
                if n%2:
                    ans=(ans+y)%mod
                else:
                    ans=(ans+d)%mod
                #x=2
                #while x<n:
                    #ans=(ans+(ncr(n,x)*y))%mod
                    #x+=2
                ans=(ans+b*y-y-y*(1 if n%2==0 else 0))%mod
                d=(d*e)%mod
                
            
            print(ans%mod)
        
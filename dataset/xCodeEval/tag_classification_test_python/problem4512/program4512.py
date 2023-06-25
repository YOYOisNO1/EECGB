def program4512():
    num,mod=map(int,input().split())
    fact=[0]*(num+2)
    fact[0]=1
    
    for i in range(1,num+1):
        fact[i]=fact[i-1]*i
        fact[i]%=mod
    
    ans=1
    for i in range(num):
        ans+=(((num-i)*fact[num-i])%mod*fact[i+1])%mod
        ans%=mod
    print(ans-1)
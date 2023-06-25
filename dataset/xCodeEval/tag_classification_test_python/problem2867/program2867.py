    mod=10**9 + 7
def inverse(i):
        return pow(i,mod-2,mod)
    fact=[1]*(10**5 + 1)
    ifact=[1]*(10**5 + 1)
    
    
    for i in range(2,10**5 + 1):
        fact[i]=fact[i-1] *i
        ifact[i]=ifact[i-1] *inverse(i)
        fact[i]%=mod
        ifact[i]%=mod
def ncr(n,k):
        ans=fact[n]*ifact[k]*ifact[n-k]
        return ans%mod
        
    
    n,x,pos=map(int,input().split())
    left=0
    right=n
    
    els=[]
    big=[]
    
    while left<right:
        middle=(left+right)//2
        if middle<=pos:
            els.append(middle)
            left=middle+1
        else:
            right=middle
            big.append(middle)
    
    # print(els,big)
    if len(els)>x or len(big)>n-x:
        print(0)
    else:
        els=len(els)-1
        big=len(big)
        ans=1
        ans*=ncr(x-1,els)
        ans%=mod
        
        ans*=ncr(n-x,big)
        ans%=mod
        
        ans*=fact[n-big-els-1]
        ans%=mod
        
        ans*=fact[els]
        ans%=mod
        
        ans*=fact[big]
        
        ans%=mod
        print(ans)
    
    # print(big,els)
        
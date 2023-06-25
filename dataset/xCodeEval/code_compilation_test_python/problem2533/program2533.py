    import sys
    sys.setrecursionlimit(100000)`
    from future import division
    range = xrange
    input = input
    
def factors(n):
        ans=[]
        if(n%2==0):
            ans.append(2)
        while(n%2==0):
            n//=2
        for i in range(3,int(n**0.5)+1,2):
            if(n%i==0):
                ans.append(i)
            while(n%i==0):
                n//=i
        if(n>2):
            ans.append(n)
        return ans
    
    
    x,n=input().split()
    x=int(x)
    n=int(n)
    factor=factors(x)
    ans=1
    for i in factor:
        if(n//i>0):
            k=0
            j=n
            while(j!=0):
                j=j//i
                k+=j
            k%=1000000006
            ans*=pow(i,k,1000000007)
            ans%=1000000007
    print(ans)
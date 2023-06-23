    from math import *
    #a,b = map(int,input().split())
def f1(a,b):
        if a==b:
            return a^a
        minp,maxp = int(log(a,2)),int(log(b,2))
        #print(2**minp,2**maxp)
        if a<2**maxp<=b:
            return (2**maxp)^(2**maxp-1)
        else:
            if b==a+1:
                return a^b
           # if 2**minp==a:
            #    return 2**(minp-1)-1
            if maxp==minp:maxp+=1
            l = 2**minp
            ans = 0
            for i in range(minp-1,0,-1):
                if l+2**i<=b:
                    l += 2**i
                    ans=max(ans,l^(l-1))
            return ans
    
def f2(a,b):
        a2 = 0
        for i in range(a,b+1):
            for j in range(a,b+1):
                if i^j>a2:
                    a2=i^j
        return a2
    
     a,b = map(int,input().split())
     print(f1(a,b))
def program3432():
    import math
    n=int(input(),2)
    if n==0:
        print(0)
    else:    
        ans=math.floor(math.log(n,4))
        if 4**ans==n or 4**ans==n+1:
            ans-=1
        print(ans+1)
    
    
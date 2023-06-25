def program1730():
    n=int(input())
    import sys
    num9=len(str(2*n))-1
    
    s=[str(i) for i in range(10)]
    ans=0
    
    if(num9==0):
        print(n*(n-1)//2)
        sys.exit()
    for i in s:
        x=i+'9'*num9
        x=int(x)
        ans+=max(0,min((n-x//2),x//2))
    print(ans)
        
        
        
        
    
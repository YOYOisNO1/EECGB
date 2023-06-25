def program5532():
    import sys
    n,k=map(int,sys.stdin.readline().split())
    l=list(map(int,sys.stdin.readline().split()))
    x=0
    c=0
    for i in range(n):
        if l[i]<=k:
            x+=1 
            c=i
        else:
            break
    for i in range(n-1,c,-1):
        if l[i]<=k:
            x+=1 
        else:
            break 
    print(x)    
        
            
            
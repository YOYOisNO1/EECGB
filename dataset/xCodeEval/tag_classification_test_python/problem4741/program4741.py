def f(tar,n,m):
        n-=m
        bir=(tar*(tar+1))//2
        if bir>=n:
            return True
        else:
            return False
    
    import sys
    
    n,m=map(int,input().split())
    if n<=m:
        print(n)
        sys.exit()
    
    low,high=0,10**18
    while(low<high):
        mid=low+(high-low)//2
        x=f(mid,n,m)
        if x:
            high=mid
        else:
            low=mid+1
    
    print(low+m)
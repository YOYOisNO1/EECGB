    
def domino(n,m):
        if n<=1 and m<=1:
            return 0
        elif n=1 and m=2:
            return 1
        elif n=2 and m=1:
            return 1
        else:    
            return 2+max(domino(n-1,m-2),domino(n-2,m-1))
    
    
    
    
    
    
    
    n,m=list(map(int,input().split()))
    print(domino(n,m))
    
def program6397():
    
    n,k=map(int,input().split())
    if k==0 or n==k:
        print(0,0)
    else:
        print(1,min(n-k,k*2))
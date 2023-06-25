def program2610():
    n,a,b=map(int,input().split())
    
    extra=max(0,a-(n-b-1))
    
    print(b+1-extra)
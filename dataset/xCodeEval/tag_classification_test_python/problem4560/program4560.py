def program4560():
    n,k = list(map(int, input().split(" ")))
    print((n//2-(n//2)%(k+1))//(k+1),((n//2-(n//2)%(k+1))//(k+1))*k,n-(n//2-((n//2)%(k+1))) if k<=n//2 else n)
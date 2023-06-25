def game(n,m):
        if n=1:
            return 1
        if m-1>=n-m:
            return m-1
        else:
            return m+1
    
    n,m=[int(i) for i in input().split()]
    print(game(n,m))
        
        
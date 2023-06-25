def program681():
    n, m = map(int, input().split())
    
    if n==0 and m>0:
        print("Impossible")
    else:
        max_rev = n + max(m-1, 0)
        min_rev = n + max(m-n, 0)
        
        print(min_rev, max_rev)
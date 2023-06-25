def program3485():
    n, k = map(int, input().split())
    
    vals = map(int, input().split())
    
    candies = 0
    bran = 0
    
    poss = False
    for i in range(n):
        candies += vals[i]
    
        togive = min(8, candies)
        bran += togive
        candies -= togive
        if bran >= k:
            print(i+1)
            poss = True
            break
    
    if not poss:
        print(-1)
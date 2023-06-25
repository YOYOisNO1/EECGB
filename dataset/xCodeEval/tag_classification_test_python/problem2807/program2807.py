def program2807():
    N = input()
    L = map(int, input().split())
    
    solve = True
    
    step = 1
    
    for i in xrange(1, N):
        if step == 1:
            if L[i] > L[i - 1]:
                continue
            else:
                step = 2
        
        if step == 2:
            if L[i] == L[i - 1]:
                continue
            else:
                step = 3
        
        if step == 3:
            if L[i] < L[i - 1]:
                continue
            else:
                solve = False
                break
    
    
    if solve:
        print("YES")
    else:
        print("NO")
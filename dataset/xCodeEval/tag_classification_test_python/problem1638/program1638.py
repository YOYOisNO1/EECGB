def program1638():
    ii = int
    a1,a2,k1,k2,n = ii(input()),ii(input()),ii(input()),ii(input()),ii(input())
    
    # makea k1<=k2
    if k1>k2:
        a1,a2,k1,k2 = a2,a1,k2,k1
    
    if n <= a1 * k1:
        big = (n//k1)
    else:
        big = (a1 + (n-a1*k1)//k2)
    
    smol = min(a1+a2,max(0, n - (a2)*(k2-1) - (a1)*(k1-1)))
    
    print(smol,big)
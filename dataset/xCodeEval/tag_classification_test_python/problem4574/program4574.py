def program4574():
    
    # s = input()
    li = input().split(' ')
    n = int(li[0])
    m = int(li[1])
    k = int(li[2])
    
    if k < n:
        print(k+1, 1)
        exit()
    elif k >= n and k <= n+m-2:
        print(n, k-n+2)
    else:
        p = m*n-k
    
        row = (p-1)//(m-1) + 1
    
        if row % 2 == 0:  # even <-
            column = (m-2) - ((p-1) % (m-1)) + 2
        else:  # odd ->
            column = (p-1) % (m-1) + 2
    
        print(row, column)
def program1593():
    n, k = list(map(int, input().split()))
    
    g = min(2 * k, n-k)
    
    if k < n && k > 0:
        print('1 ' + str(g))
    else:
        print('0' + str(g))
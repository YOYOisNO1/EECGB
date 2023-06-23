def program1273():
    # 1062B
    #   greedy      math      number theory      *1600
    
    '''
    给定一个正整数n，有两种操作：
    1、乘以任意一个正整数x， n=n*x
    2、开平方根, n=sqrt(n)
    问最少几次操作后，n最小，是多少
    '''
    
    import math
    
    n = int(input())
    ans, anssq = 1, 0
    maxsq = 1
    tempn = n
    for i in range(2, n + 1):
        tempsq = 0
        while tempn % i == 0:
            tempn //= i
            tempsq += 1
        if tempsq > 0:
            ans *= i
        if tempsq > maxsq:
            maxsq = tempsq
    print(ans, math.ceil(math.log2(maxsq) + 1))
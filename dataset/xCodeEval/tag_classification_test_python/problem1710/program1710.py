def program1710():
    # n coins, value of 1
    # 1 <= x <= n
    # packets can contain any amount of x
    
    # input
    n = int(input().rstrip())
    
    
    count = 0
    mSum = 0
    
    for i in range(n):
        mSum = 2 ** i
        count += 1
        if mSum > n:
            count -= 1
            break
    
    print(count)
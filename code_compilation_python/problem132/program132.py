def program132():
    k = int(input())
    
    if k > 37:
        print(-1)
    else:
        x = ""
        for i in range(k//2):
            x += '8'
        if k % 2:
            x += '6'
    
        print(x)
    
    # 1000000000000000000
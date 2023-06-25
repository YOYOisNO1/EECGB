def program1202():
    import math
    
    
    l, r, x, y, k = map(int, input().split())
    la, ra = k * x, k * y
    
    if r < la or ra < l:
        print('NO')
    elif l <= la <= r or l <= ra <= r:
        print('YES')
    else:
        xb = int(math.floor(l / k))
        yb = int(math.ceil(r / k))
        # print(xb, yb)
        for b in range(xb, yb + 1):
            if l <= k * b <= r:
                print('YES')
                break
        else:
            print('NO')
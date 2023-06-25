def program362():
    x, y = map(int, input().split())
    
    if x < y:
        print(0)
    elif x == y:
        print('infinity')
    else:
        z = x-y
        cnt = 0
    
        max_val = int(z**.5)
        for k in range(1, max_val+1):
            if z % k == 0:
                if k > y:
                    cnt += 1
                if z/k > y and z/k != k:
                    cnt += 1
        print(cnt)
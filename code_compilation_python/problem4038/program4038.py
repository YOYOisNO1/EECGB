def program4038():
    import math
    
    k = int(input())
    
    
    n = int(k/3)*2 + 1
    # print('n', n)
    ans = 0
    
    while True:
        point_to_check = (n+2)//2
        # print('p', point_to_check)
    
        x = 0.0
        y = n# *math.sqrt(3)
    
        # print('r', math.sqrt((x**2+y**2)))
    
        # p1
        x -= 0.5
        y += 0.5 #* math.sqrt(3)
    
        # print('r', math.sqrt((x**2+y**2)))
    
        count = -1
        for i in range(point_to_check):
            # print('r', math.sqrt((x**2+y**2)))
            if ((x**2+3*(y**2))<=k**2):
                count = i
                break
            x -= 1.5
            y -= 0.5 # * math.sqrt(3)
    
        extra = 0
        if count != -1:
            extra = point_to_check - count
    
            if (n+1)%2==0:
                extra *= 2
            else:
                extra = extra*2 -1
    
            if extra == n+1:
                ans += (extra-1)*6
                break
            else:
                ans += extra*6
    
        # print('n', n, 'ans', ans)
    
        n = n-1
    
    # print('extra', extra)
    
    
    
    for i in range(n):
        if i==0:
            ans += 1
        else:
            ans += i*6
    
    
    if k<=2:
        print(1)
    else:
        print(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # R = 1
    # r = sqrt(3)*0.5*R
    # full_cycle_count =  k / (math.sqrt(3)) - 0.5
    # print(full_cycle_count)
    # full_cycle_count = int(full_cycle_count)
    # print(full_cycle_count)
    #
    # half_cycle_count = int((k - 1) / 3) * 2
    # print(half_cycle_count)
    #
    # ans = 1
    # last_add = 0
    # for i in range(1, full_cycle_count+1):
    #     last_add +=6
    #     ans += last_add
    #
    # print(last_add)
    #
    # if half_cycle_count>full_cycle_count:
    #     ans += (last_add+6) / 2
    #
    # print(int(ans))
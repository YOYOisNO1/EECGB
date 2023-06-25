def program127():
    import math
    nums = input().split(" ")
    N = int(nums[0])
    P = float(nums[1])
    t = int(nums[2])
    if t <= N:
        print(round(t * P, 6))
    elif P == 1:
        print(t)
    elif P == 0:
        print(0)
    else:
        a = math.pow((1 - P),t)
        total = 0
    
        
        for i in range(1,min(N + 1, t + 1)):
            a *= ((((t + 1 - i) / i) / (1 - P)) * P)
            total += i * a
        
        for j in range(min(N + 1, t + 1), t + 1):
            a *= ((((t + 1 - j) / j) / (1 - P)) * P)
            total += N * a
        print(round(total,6))
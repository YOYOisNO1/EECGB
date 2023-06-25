def program1983():
    n, m, k = tuple(int(_) for _ in input().split())
    
    extra_pillows = m - n
    max_pillow = 1
    
    if n == 1:
        print(m)
    elif n == 2:
        if m % 2 == 0:
            print(int(m / 2))
        else:
            print(int(m / 2) + 1)
    else:
        for i in range(extra_pillows):
            step_pillows = 1 + min(k - 1, i) + min(n - k, i)
            if extra_pillows >= step_pillows:
                extra_pillows -= step_pillows
                max_pillow += 1
            else:
                break
    
        print(max_pillow)
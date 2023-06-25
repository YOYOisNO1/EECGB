def program5511():
    a, x, y = map(int, input().split())
    
    if -a / 2.0 < x < a / 2.0 and 0 < y < a:
        print(1)
    elif -a < x < 0 and y % a != 0 and y / a % 2 == 0:
        k = y / a / 2
        if k != 0: print(3) * k
        else: print(-1)
    elif -a / 2.0 < x < a / 2.0 and y % a != 0 and y / a % 2 == 1:
        k = y / a / 2
        print(3) * k + 2
    elif 0 < x < a and y % a != 0 and y / a % 2 == 0:
        k = y / a / 2
        if k != 0: print(3) * k + 1
        else: print(-1)
    else:
        print(-1)
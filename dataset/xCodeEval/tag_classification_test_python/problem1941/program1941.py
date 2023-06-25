def program1941():
    a, b = [int(i) for i in input().split()]
    if a == 9 and b == 1:
        print(f'9 10')
    elif abs(b - a) > 1 or a - b == 1:
        print(-1)
    elif b - a == 1:
        print(f'{a}99 {b}00')
    else:
        print(f'{a}00 {b}01')
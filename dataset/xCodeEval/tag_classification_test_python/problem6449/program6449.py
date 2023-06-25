def program6449():
    n = int(input())
    a = int(input())
    b = int(input())
    if 2 * (2 * a + b) <= n:
        print(1)
    elif 2 * a + b <= n:
        print(2)
    elif 4 * a <= n and 2 * b <= n:
        print(2)
    elif 2 * a <= n and b * 2 <= n:
        print(3)
    elif a + b <= n and 2 * a <= n:
        print(3)
    elif 4 * a <= n and b * 2 > n:
        print(3)
    elif 2 * a <= n:
        print(4)
    elif a + b <= n:
        print(4)
    elif b * 2 <= n:
        print(5)
    else:
        print(6)
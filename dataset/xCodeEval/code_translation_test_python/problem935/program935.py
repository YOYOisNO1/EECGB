def program935():
    x, y = [int(x) for x in input().split()]
    n = int(input())
    tmp = 0
    if n % 6 == 1:
        tmp = x
    elif n % 6 == 2:
        tmp = y
    elif n % 6 == 3:
        tmp = y - x
    elif n % 6 == 4:
        tmp = -x
    elif n % 6 == 5:
        tmp = -y
    elif n % 6 == 0:
        tmp = -y + x
    print(tmp % (10**9 + 7))
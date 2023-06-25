def program6036():
    n, m = (int(x) for x in input().split())
    if m == 1:
        print(n)
    else:
        p = 0
        while n != 0:
            p += 1
            n //= 2
        print(2 ** p - 1)
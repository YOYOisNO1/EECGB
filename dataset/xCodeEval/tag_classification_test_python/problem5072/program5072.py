def program5072():
    n = int(input())
    a = n // 4
    if n % 2 != 0:
        print(0)
    elif n % 4 == 0:
        print(a - 1)
    else:
        print(a)
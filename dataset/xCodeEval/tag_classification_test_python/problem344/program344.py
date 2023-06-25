def program344():
    n = int(input())
    if n == 1:
        print(3)
    elif n % 3 == 2:
        print(4 * (n // 3) + 5)
    elif n % 3 == 0:
        print(4 * (n // 3) + 3)
    else:
        print(4 * (n // 3 + 1))
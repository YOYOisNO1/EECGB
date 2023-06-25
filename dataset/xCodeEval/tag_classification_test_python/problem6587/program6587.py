def program6587():
    from math import ceil, sqrt
    x = int(input())
    if x == 3:
        print(5)
    else:
        print(2 * (ceil(sqrt(2 * x - 1)) // 2) + 1)
def program6400():
    n, k = map(int, input().strip().split())
    answ = 0
    flag = False
    if k == 0 or n == k:
        print(0, 0)
    else:
        if n // 3 >= k:
            print(1, k * 2)
        else:
            print(1, n - k)
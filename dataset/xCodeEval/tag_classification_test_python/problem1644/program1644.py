def program1644():
    n,k = map(int,input().split(' '))
    if k > 2 * n - 1:
        print('0')
    else:
        if n >= k:
            print((k - 1) // 2)
        else:
            if k & 1:
                print(n - (k - 1) // 2)
            else:
                print(n - k // 2)
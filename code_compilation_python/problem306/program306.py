def program306():
    
    input()
    b = list(map(int, input().split()))
    a = list(sorted(set(b)))
    if len(a) == 3:
        if (a[2] - a[1]) == (a[1] - a[0]):
            print(a[1] - a[0])
        else:
            print(-1)
    elif len(a) == 1:
        print(0)
    else:
        if (a[1] - a[0]) % 2 == 0:
            print((a[1] - a[0]) // 2)
        else:
            print(a[1] - a[0])
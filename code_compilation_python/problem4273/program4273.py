def program4273():
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        print(a[0])
    elif n == 2:
        print(a[1] + (a[1]-a[0]))
    else:
        f = True
        d = a[1]-a[0]
        for i in range(1, n):
            if (a[i] - a[i-1] != d)
                f = False
        if f:
            print(a[-1]+d)
        else:
            print(a[-1])
def program653():
    m, n, a = map(int, input().split())
    if a > m and a >n:
        print(1)
    else:
        k1=int(round(m/a+ 0.499999999))
        k2=int(round(n/a+ 0.499999999))
        if a == 1 :
            print(m*n)
        else:
            print(int(k1*k2))
def program839():
    v1 , v2 = map(int , input().split(' '))
    t , d = map(int , input().split(' '))
    a = [0] * (t + 1)
    a[0] = v1
    a[t - 1] = v2
    cvb = 0
    for i in range(1 , t - 1):
        a[i] = min(a[i - 1] + d , v2 + (t - i - 1) * d)
        cvb += a[i]
    print(cvb + v1 + v2)
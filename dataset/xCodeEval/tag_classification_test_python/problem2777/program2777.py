def program2777():
    n, m, k = map(int, input().split())
    a = 1000000009
    
    udv = m - n + n / k
    if udv <= 0:
        print(m)
    else:
        x = (pow(2, udv + 1, a) - 2) * k
        print((x) + m - udv * k ) % a
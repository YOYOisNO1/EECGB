def program32():
    d, L, v1, v2 = map(int, input().split(' '))
    
    whole = 0
    while L > d:
        L -= (v1 + v2)
        whole += 1
    
    t = float(L-d) / float(v1 + v2)
    print(whole) + t
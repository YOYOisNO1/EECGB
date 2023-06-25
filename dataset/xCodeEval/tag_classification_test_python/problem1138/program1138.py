def program1138():
    n, m, k = map(int, input().split())
    l = (k-1)/(2*m) + 1
    d = (k - (l-1)*m*2 - 1)/2 + 1
    if k % 2 == 0:
        s = 'R'
    else:
        s = 'L'
    print(l,) d, s
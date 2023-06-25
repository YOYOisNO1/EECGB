def program1733():
    L=lambda:map(int,input().split())
    l, r, x, y, k = L()
    for b in range(max(x,l/k), min(y,r/k)+1):
        if l <= b * k <= r:
            print('YES')
            exit()
    print('NO')
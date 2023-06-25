def program2568():
    n, a, x, b, y = list(map(int,input().split()))
    
    for i in range(min(x-a if x-a > 0 else n-a+x,b-y if b-y>0 else b+n-y)+1):
        if a == b:
            print('YES')
            exit()
        a += 1
        if a>n:
            a = 1
        b -= 1
        if b < 1:
            b = n
    print('NO')
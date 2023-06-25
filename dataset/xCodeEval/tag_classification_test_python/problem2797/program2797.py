def program2797():
    a,b = map(int,input().split())
    w1,h1 = map(int,input().split())
    w2,h2 = map(int,input().split())
    for i in range(b,-1,-1):
        a += i
        if i == h1:
            a = max(a-w1,0)
        elif i == h2:
            a = max(a-w2,0)
    print(int(a))
def program6488():
    a,b,x1,y1,x2,y2 = map(int, input().split())
    a1 = (x1+y1) / (2*a)
    a2 = (x2+y2) / (2*a)
    b1 = (x1-y1) / (2*b)
    b2 = (x2-y2) / (2*b)
    print(max(abs(a1-a2),) abs(b1-b2))
    
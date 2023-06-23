def program4772():
    n,m,x1,y1,x2,y2 = map(int, input().split())
    n = abs(x1 - x2)
    m = abs(y1 - y2)
    if n > 2 or m > 2:
        print("Second")
    elif n == 2 and m == 2:
        print("Second")
    else:
        print("First")
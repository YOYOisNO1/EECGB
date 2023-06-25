def program466():
    l = list(map(int , input().split()))
    l.sort()
    a,b,c,d = l
    if b + c > d or a + b > c :
        print("TRIANGLE")
    elif b + c = d or a + b = c:
        print("SEGMENT")
    else:
        print("IMPOSSIBLE")
        
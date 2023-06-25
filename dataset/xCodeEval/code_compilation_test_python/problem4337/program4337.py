def program4337():
    a,b,x1,y1,x2,y2 = map(int,input().split())
    s = (x1 + y1) // (2 * a) - (x2 + y2) // (2 * a)
    s += (x1 - y1) // (2 * b) - (x2 - y2) // (2 * b)
    print(s)
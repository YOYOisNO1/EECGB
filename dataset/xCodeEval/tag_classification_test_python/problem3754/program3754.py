def program3754():
    x, y = [int(x) for x in input().split()]
    b = y - 1
    a = (x-b)/2
    print("Yes" if a>=0 and b>=0 and (a==0 or b>0) and a==int(a) else "No")
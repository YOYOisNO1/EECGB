def program5619():
    a,b = map(int,input().split())
    
    if a > b:
        t = a
        a = b
        b = t
    
    if a == 1:
        print(b)
    elif a == 2:
        print((b) / 4 * 2 + min(b % 4,2)) * 2
    else:
        print(a) * b + 1 >> 1
    
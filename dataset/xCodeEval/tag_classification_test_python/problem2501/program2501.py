def program2501():
    a, b, c = [int(i) for i in input().split()]
    
    if (c == 0):
        if (a == b):
            print("YES")
        else:
            print("NO")
    elif ((b - a) % c == 0):
        if ((b - a) / c >= 0):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
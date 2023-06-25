def program3775():
    import sys
    
    a = [[int(x) for x in input().split()] for _ in range(4)]
    
    if a[0][3] and (a[1][0] or a[2][1] or a[3][2]):
        print("YES")
    elif a[1][3] and (a[2][0] or a[3][1] or a[0][2]):
        print("YES")
    elif a[2][3] and (a[3][0] or a[0][1] or a[1][2]):
        print("YES")
    elif a[3][3] and (a[0][0] or a[1][1] or a[2][2]):
        print("YES")
    else:
        for i in range(4):
            if a[i][3] and (a[i][0] or a[i][1] or a[i][2]):
                print("YES")
                sys.exit(0)
        print("NO")
def program2128():
    a = [map(int, input().split()) for _ in xrange(4)]
    a.extend(a)
    for i in xrange(4):
        if (a[i][0] and a[i-1][3]) or (a[i][1] and a[i+2][3]) or (a[i][2] and a[i+1][3]):
            print("YES")
            quit()
    print("NO")
    
    
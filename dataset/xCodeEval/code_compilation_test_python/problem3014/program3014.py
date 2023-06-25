def program3014():
    y,x = map(int,input().split())
    if y==2 || y ==3:
        print("YES")
        quit()
    while x != 0:
        u = x % y
        #print u
        if u != y - 1 and u != 0 and u != 1:
            print("NO")
            quit()
        if u == y - 1:
            x += 1
        else:
            x /=y
    print("YES")
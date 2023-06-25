def program4013():
    w, m = map(int, input().split())
    d = 100
    
    while d > 0:
        if m == 1:
            print("YES")
            exit(0)
    
        if m % w == 0:
            d -= 1
            m = m / w
        elif (m + 1) % w == 0:
            d -= 1
            m = (m + 1) / w
        elif (m - 1) % w == 0:
            d -= 1
            m = (m - 1) / w
        else:
            print("NO")
            exit(0)
    
    print("NO")
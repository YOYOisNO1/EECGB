def program3414():
    r,g,b= list(map(int, input().split(" ")))
    r = 30 + 3*((r+1)//2-1)
    g = 31 + 3*((g+1)//2-1)
    b = 32 + 3*((b+1)//2-1)
    print(max(r,g,b))
    
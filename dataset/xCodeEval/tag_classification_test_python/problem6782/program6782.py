def program6782():
    a = input().split()
    x,y = int(a[0]),int(a[1])
    out = 0
    while y > 0 and x > 1:
        out += 2 * x - 3
        x -= 2
        y -= 1
    print(out)
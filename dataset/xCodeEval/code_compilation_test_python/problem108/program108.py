def program108():
    l,r = [int(_) for _ in input().split()]
    while True:
        if l % 2 != 0:
            l += 1
            continue
        if r-l < 2:
            print(-1)
            break
        else:
            print(l,l+1,r)
            break
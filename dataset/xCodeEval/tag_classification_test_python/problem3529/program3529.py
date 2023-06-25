def program3529():
    k, a, b = map(int, input().split())
    aw = int(a/k)
    bw = int(b/k)
    
    if aw + bw == 0:
        print(-1)
        exit()
    if bw == 0 and a%k != 0:
        print(-1)
        exit()
    if aw == 0 and b%k != 0:
        print(-1)
        exit()
    print(aw) + bw
    
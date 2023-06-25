def program197():
    n, d = map(int, input().split())
    
    lilies = input()
    
    pos = 0
    jumps = 0
    while True:
        target = lilies.rfind("1", pos + 1, pos + d + 1)
        jumps += 1
    
        if target == -1:
            print(-1)
            break
        else:
            if target == n - 1:
                print(jumps)
                break
        pos = target
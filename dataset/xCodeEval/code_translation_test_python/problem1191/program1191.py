def program1191():
    n, k = list(map(int,input().split()))
    devs = []
    iter = 1
    while iter*iter <= n:
        if n%iter == 0:
            if iter*iter == n:
                devs.append(iter)
            else:
                devs.append(iter)
                devs.append(n//iter)
        iter+=1
    devs.sort()
    
    if k > len(devs):
        print(-1)
    else:
        print(devs[k-1])
def program3():
    x, y = map(int, input().split(' '))
    
    t = [y, y, y]
    goal = 3 * x
    
    finish = False
    cnt = 0
    while not finish:
        for i in range(3):
            cnt += 1
            t[i] = min(sum(t) - t[i] - 1, x)
            if sum(t) == goal:
                finish = True
                break
    
    print(cnt)
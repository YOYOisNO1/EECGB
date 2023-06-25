def program2661():
    p, y = map(int, input().split(' '))
    
    cur = y
    while cur > p:
        i = 2
        while i ** 2 <= cur and i <= p:
            if cur % i == 0:
                break
            i += 1
        else:
            print(cur)
            exit(0)
    
        cur -= 1
    
    print(-1)
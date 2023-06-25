def program3985():
    w, m = [int(i) for i in input().split()]
    
    
    k = 0
    while k <= 100:
        if(m == 0):
            print('YES')
            exit(0)
        d = m % (w)
        if d == 0:
            m = m/w
            k += 1
        elif d == 1:
            k+=1
            m = (m-1)/w
        elif d == w-1:
            m = (m+1)/w
            k+=1
        else:
            print('NO')
            exit(0)
    print('NO')
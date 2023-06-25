def program972():
    n, m = map(int, input().split())
    
    if n == m:
        print(0)
    
    elif m % n != 0:
        print(-1)
    
    else:
        k = m // n
        if k % 2 != 0 and k % 3 != 0:
            print(-1)
        else:
            p, q = 0, 0
            while(k % 2 == 0):
                p += 1
                k /= 2
            while(k % 3 == 0):
                q += 1
                k /= 3
            if k != 1:
                print(-1)
            else:
                print(p + q)
def program3213():
    #!/bin/python3
    import math
    n = int(input())
    
    for rd in range(n):
        my , tot , p , q = list(map(int , input().split()))
        m = 0
        if(tot % q == 0):
            m = tot // q
        else:
            m = (tot // q + 1)
    
        np = m * p ; nq = m * q
        for i in range(500000):
            if(np - my <= nq - tot and np - my >= 0):
                print(nq - tot)
                break
            np += p ; nq += q
            if(p == 1 and q == 1):
                print(-1)
                break
        else:
            print(-1)
    
    
    #    for i in range(1000000):
    #        if(tot % q == 0):
    #            if((p * tot / q) == my):
    #                print(i)
    #                break
    #        if(my / tot > p / q):
    #            tot += 1
    #        else:
    #            tot += 1; my += 1
    #        if(p == 1 and q == 1):
    #            print(-1)
    #            break
    #        if(p == 0 and q == 0):
    #            print(-1)
    #            break
    #    else:
    #        print(-1)
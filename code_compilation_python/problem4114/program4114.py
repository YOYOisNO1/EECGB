def program4114():
    p,k = map(int,input().split())
    M = 1000000007
    
    if k == 0:
        print pow(p, p-1, M)
    elif k == 1:
        print pow(p, p, M)
    else:
        m = 1
        for i in range(1,p+1):
            if pow(k, i, p) == 1:
                m = i
                break
        print pow(p, (p-1)/m, M)
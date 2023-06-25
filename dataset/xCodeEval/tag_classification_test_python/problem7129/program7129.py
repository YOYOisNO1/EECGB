def program7129():
    p,k = map(int,input().split())
    m = 10**9+7
    if k == 0:
        print(pow(p,p-1,m))
    elif k == 1:
        print(pow(p,p,m))
    else:
        used = [0]*p
        res = 0
        for i in range(1, p):
            a = i
            
            if used[a] == 0:
                res += 1
            while used[a] == 0:
                used[a] = 1
                a = k * a % p
        print(pow(p, res, m))
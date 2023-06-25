def program2689():
    n,m,k = map(int,input().split())
    p = 2*(n + m - 2)
    m-=6; n -= 4; l = 1
    while m > 0 and n > 0 and l < k:
        p += 2*(n + m); n-= 4; m-= 4; l += 1
    print(p)
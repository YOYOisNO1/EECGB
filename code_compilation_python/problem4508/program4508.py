def program4508():
    p = 10**9+7
    n, m, k, r, c = [int(x) for x in input().split()]
    ax, ay, bx, by = [int(x) for x in input().split()]
    answer = pow(k, n*m-r*c, p)
    print(answer)    
        
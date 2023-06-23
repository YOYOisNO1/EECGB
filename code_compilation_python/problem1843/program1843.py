def program1843():
    n, k, l, c, d, p, nl, np = [int(i) for i in input().split()]
    print(min((k*l)//(n*nl), c*d//n, p//(n*np))
def program7267():
    N,M = (int(x) for x in input().split())
    if N > 1 or M > 1:
        sol = 1/float(N) + (N-1)*(M-1) / float((N*(N*M-1)))
    else:
        sol = 1.0000
    print(sol)
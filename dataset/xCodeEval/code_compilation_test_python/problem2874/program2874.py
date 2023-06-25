def program2874():
    n, k = [*map(int, input().split())]
    M = 998244353
    C = [[1]]
    for i in range(n): C.append([1]+[(C[-1][j]+C[-1][j+1])%M for j in range(i)]+[1])
    d = [0]*(n+1)
    d[1]=1
    for i in range(1, k+1):
        for j in range(1, n+1):
            d[j] = sum(d[j-x]*C[j-1][x]*pow(k-i+1,x*(x-1)//2+x*(j-1-x),M)%M for x in range(j))%M
    print(d[n])
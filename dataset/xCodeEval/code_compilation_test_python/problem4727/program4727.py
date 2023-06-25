def xor(i, j):
        if i == 0:
            return p[j]
        return p[j] ^ p[i - 1]
    
    
    n = int(input())
    u = list(map(int, input().split()))
    p = u[:]
    
    k = 32
    ans = 1000000000000
    for i in range(n):
        for j1 in range(i, max(-1, i - k - 1), -1):
            for j2 in range(i + 1, min(n, i + k + 1)):
                x1 = xor(j1, i)
                x2 = xor(i + 1, j2)
                #print(x1, x2, j1, i, j2)
                if x1 > x2:
                    ans = min(ans, j2 - j1 - 1)
    if ans == 1000000000000:
        print(-1)
    else:
        print(ans)
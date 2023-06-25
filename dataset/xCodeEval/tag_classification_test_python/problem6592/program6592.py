def program6592():
    from collections import *
    n, s, k = map(int, input().split())
    s -= 1
    a = map(int, input().split())
    C = input()
    DP = [defaultdict(int) for _ in range(n*n)]
    for i in range(n):
        DP[abs(i-s)][i] = a[i]
    for t in range(n*n):
        for i, v in DP[t].items():
            if v >= k:
                print(t)
                exit()
            for j in range(n):
                if a[j] > a[i] and C[j] != C[i]:
                    DP[t + abs(j-i)][j] = max(DP[t+abs(j-i)][j], v + a[j])
    
    print(-1)
    
    
    
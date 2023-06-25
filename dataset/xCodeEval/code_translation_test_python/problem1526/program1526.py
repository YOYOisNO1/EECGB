def program1526():
    import sys
    
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    ans = 0
    F = [1] * (n + 1)
    for i in range (0, n):
        F[i + 1] = F[i] * (i + 1) % m
    
    for i in range (0, n):
        ans = (ans + (n - i) * (n - i) * F[n - i - 1] * F[i+1]) % m
    
    print(ans)
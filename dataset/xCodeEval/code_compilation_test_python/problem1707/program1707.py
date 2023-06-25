def program1707():
    n, k, m, d = map(int, input().split())
    ans = 0
    for i in range(1, d+1):
        hi = min(m, n//(k*(i-1)+1), lo = n//(k*i+1)
        if(hi > lo) ans = max(ans, i*hi)
    print(ans)
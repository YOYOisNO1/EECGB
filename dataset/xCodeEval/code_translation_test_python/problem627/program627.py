def program627():
    mp = lambda: map(int, input().split())
    n, k = mp()
    for ans in range(1000):
        if 2*ans + (n-ans)*3 <= k:
            break
    print(ans)
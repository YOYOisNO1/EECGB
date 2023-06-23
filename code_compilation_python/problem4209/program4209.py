def program4209():
    N = int(input())
    ans = (N+1) // 2 - 1
    if N % 2 == 0:
        ans = max(0, ans-1)
    print(ans)
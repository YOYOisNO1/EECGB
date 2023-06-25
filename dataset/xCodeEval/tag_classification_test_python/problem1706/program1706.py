def program1706():
    n, m = list(map(int, input().split()))
    ans = min(max(1, m), n-m)
    print(ans)
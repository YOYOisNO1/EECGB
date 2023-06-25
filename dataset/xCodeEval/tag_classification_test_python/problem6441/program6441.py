def program6441():
    n = int(input())
    ans = 0
    for c in range(1, n + 1):
        for b in range(c // 2, c):
            if   c - b < b ^ c <= b:
                ans += 1
    print(ans)
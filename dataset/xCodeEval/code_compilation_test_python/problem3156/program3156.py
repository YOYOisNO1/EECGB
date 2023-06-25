def program3156():
    n, m = map(int, input().split())
    ans = (n * m) // 5
    if (n * m) % 5 == 4 || (n * m) % 5 == 1:
        ans += 1
    print(ans)
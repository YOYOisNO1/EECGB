def program5802():
    n = int(input())
    a = list(map(int, input().split()))
    c = a.count(min(a))
    print('Alice' if c <= n // 2 else 'Bob')
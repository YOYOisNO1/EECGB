def program451():
    s = sum(map(int, input().split()))
    print(s) / 5 if s % 5 == 0 and s > 0 else -1
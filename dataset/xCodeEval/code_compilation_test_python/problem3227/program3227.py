def program3227():
    K, a, b = map(int, input().split())
    if a >= K and b >= K:
        print(a\K + b\K)
    elif a >= K and b < K:
        print(-1 if a%K != 0 else a\K)
    elif a < K and b >= K:
        print(-1 if b%K != 0 else b\K)
    else:
        print(-1)
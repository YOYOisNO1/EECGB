def program3004():
    n, k, x = map(int, input().split())
    a = map(int, input().split())
    
    if (k == n):
            print(k * x)
    else:
            print(sum(a[: n - k]) + (k * x))
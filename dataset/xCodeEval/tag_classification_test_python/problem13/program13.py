def program13():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    print("NO" if sum(arr) - max(arr) > s else "YES")
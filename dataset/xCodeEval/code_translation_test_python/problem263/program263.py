def program263():
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    m = int(input())
    print(sum(arr[:m]) if m <= n else sum(arr) - d * (m-n))
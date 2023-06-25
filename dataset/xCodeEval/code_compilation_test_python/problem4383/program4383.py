def program4383():
    R = lambda: map(int, input().split())
    n = int(input())
    arr = [1, 2] + [0] * n
    for i in range(2, n):
        arr[i] = arr[i - 1] + arr[i - 2]
    for i in range(n):
        arr[i] = (arr[i] + arr[i - 1]) % 1000000007
    print(arr[n - 1])
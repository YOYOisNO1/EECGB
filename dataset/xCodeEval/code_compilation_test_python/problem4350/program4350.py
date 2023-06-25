def program4350():
    n, m, c, d = map(int, input().split())
    arr = [0] * 20
    for i in range(c, n):
        arr[i] = arr[i - c] + d
    
    for l in range(0, m):
        a, b, c, d = map(int, input().split())
        for i in range(0, a/b):
            j = n
            while(j > c):
                arr[j] = max(arr[j], arr[j - c] + d)
                j -= 1
    print arr[n]
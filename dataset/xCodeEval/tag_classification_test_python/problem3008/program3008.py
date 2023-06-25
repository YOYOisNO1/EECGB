def program3008():
    n, k, x = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    
    for i in range(n - k, n):
        a[i] = x
    
    print(sum(a))
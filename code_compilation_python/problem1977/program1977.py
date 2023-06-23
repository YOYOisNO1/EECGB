def program1977():
     n, k = map(int, input().split())
    num = float("inf")
    for i in range(1, k):
        if n // i > 0:
            x = n // i * k + i
        if x // k * i == n:
            num = min(x, num)
    
    print(num)
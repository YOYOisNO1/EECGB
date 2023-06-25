def program1288():
    n, p = map(int, input().split())
    
    i = 0
    while True:
        if n - p * i < 0:
            print(-1)
            break
    
        if bin(n - p * i).count('1') <= i and i <= n - p * i:
            print(i)
            break
        
        i += 1
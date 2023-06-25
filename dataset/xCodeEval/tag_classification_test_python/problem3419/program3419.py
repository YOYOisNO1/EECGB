def program3419():
    n, m = map(int, input().split())
    
    a = n + 1
    b = n//2 + (n % 2)
    
    for i in range(b, a):
        if (i % m == 0):
            print(i)
            quit()
    
    print(-1)
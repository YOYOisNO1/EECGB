def program1948():
    I = lambda: map(int, input().split())
    
    n, _, _ = I()
    A = set(I())
    I()
    
    print(*(2 - (i in A) for i in range(1, n+1)))
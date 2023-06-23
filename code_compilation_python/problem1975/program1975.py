def program1975():
    n, k = map(int, input().split())
    
    j = k-1
    # Ищем MAX x%k
    while j > 1:
        if n%j == 0:
            break
        j-=1
        
    x = (n//j)*k + j
    
    print(x)
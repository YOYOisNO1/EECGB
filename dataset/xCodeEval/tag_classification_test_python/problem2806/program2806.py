def program2806():
    from sys import stdin
    
    n = int(stdin.readline().strip())
    a = map(int, stdin.readline().strip().split())
    
    i = 1
    while i < n and a[i] > a[i-1]:
        i += 1
        
    while i < n and a[i] == a[i-1]:
        i += 1
        
    while i < n and a[i] < a[i-1]:
        i += 1
        
    if i < n:
        print('NO')
        quit()
        
    print('YES') 
def program218():
    n = input().split()
    for i in range(4):
        n[i] = int(n[i])
        
        
    if n[0] + n[1] == n[2] + n[3]:
        print('YES')
        
    elif n[0] + n[2] == n[1] + n[3]:
        print('YES')
        
    elif n[0] + n[3] == n[2] + n[1]:
        print('YES')
        
    elif n[0] == n[2] + n[1] + n[3]:
        print('YES')
        
    elif  n[1] == n[2] + n[0] + n[3]:
        print('YES')
        
    elif n[2] == n[0] + n[1] + n[3]:
        print('YES')
        
    elif n[3] == n[0] + n[1] + n[2]:
        print('YES')
    
    else:
        print('NO')
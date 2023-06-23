def program3693():
    l = list(map(int,input().split()))
    N = l[0]
    M = l[1]
    
    if M == 0:
           return 'YES'
    
    num = int(N//M)
    
    
    if num%2 == 0:
           print('YES')
    else:
           print('NO')
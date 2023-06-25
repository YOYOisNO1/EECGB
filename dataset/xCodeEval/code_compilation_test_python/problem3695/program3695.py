def program3695():
    N, M = int(input()).split()
    
    num = int(N//M)
    if num%2 == 0:
           print('YES')
    else:
           print('NO')
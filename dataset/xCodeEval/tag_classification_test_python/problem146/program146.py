def prime(n):
        j = 2
        s = 0
        while j <= int(n / 2):
            if n%j== 0:
                s=1
                break
            j = j + 1
        if s == 0:
            return 1
        else:
            return 0
    
    
    nn = input()
    nn = nn.split()
    n = int(nn[0])
    m = int(nn[1])
    i = n + 1
    while i > 0:
        pp=prime(i)
        if pp==1 and i==m:
            print('YES')
            break
        elif pp==1 and i!=m:
            print('NO')
            break
        i=i+1
    
    
    
    
def program4619():
    n, k = [int(x) for x in input().split()]     
    a = [ord(x) for x in list(input())]     
    b = [0] * 32
    for i in a:
        b[i - 65] += 1
    c = [0] * 32
    i = 0
    f = 0
    for i in a:
        c[i - 65] += 1
        if c[i - 65] == 1:
            k -= 1
            if k < 0:
                f = 1  
                break
        if c[i - 65] == b[i - 65] :
            k += 1
    if f == 1:
        print('YES')
    else: 
        print('NO')
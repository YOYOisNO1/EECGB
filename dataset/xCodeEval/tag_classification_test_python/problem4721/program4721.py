def program4721():
    import math
    
    q = int(input())
       
    c = 0
    ans = 1
    while q % 2 == 0:
        q //= 2
        if c == 2:
            print("1\n"+str(ans), '')
            exit()
        c +=1
        ans *= 2
    
    for i in range(3, int(math.sqrt(q)+1), 2):
        while q%i == 0:
            q //= i
            if c == 2:
                print("1\n"+str(ans), '')
                exit()
            c+=1
            ans *=i
    if q > 2:
        if c == 2:
                print("1\n"+str(ans), '')
                exit()
        c += 1
    if c <= 1:
        print('1\n0', '')
    else:
        print('2')
    
    
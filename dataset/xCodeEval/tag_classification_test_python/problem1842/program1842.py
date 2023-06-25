def program1842():
    n, m = [int(i) for i in input().split()]
    
    if m % n != 0:
        print('-1')
        exit(0)
    
    multiple = m//n
    
    count2 = 0
    while (multiple % 2 == 0):
        count2 += 1
        multiple /= 2
    
    count3 = 0
    while (multiple % 3 == 0):
        count3 += 1
        multiple /= 3
    
    csum = count2+count3
    if multiple == 1:
        print(csum)
    else:
        print('-1')
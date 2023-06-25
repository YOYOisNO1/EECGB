def program318():
    n = input()
    k  = input()
    
    sum1 = 0
    for i in range(0, len(k)-2):
        s = k[i:i+3:]
        if s == 'xxx':
            sum1 += 1
    print(sum1)
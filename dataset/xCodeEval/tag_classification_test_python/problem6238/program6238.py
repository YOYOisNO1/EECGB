def calc(n):
        if n <= 1:
            return 2**n
        
        a = calc(n/2)
        b = a
        if n%2 == 1:
            b *= 2
        return (a*b) %MOD
    
    '''den = [1]
    num = [1]
    n = int(input())
    for i in range(n):
        num.append(3*num[-1] + den[-1]-num[-1])
        den.append(4*den[-1])
        
    print(num)
    print(den''')
    
    MOD = 1000000007
    n = int(input())
    if n == 0:
        print(1)
        
    else:
        #print(((1<<(n-1))) * (1+ (1<<n)))%MOD
        #print((2**(n-1)) * (1+2**n)) %MOD
        #z = 1<<(n-1)
        #print((z) + (z<<(n))) %MOD
        #print(((1<<(n-1))) + (1<<(2*n-1))) %MOD
        
        a = calc(n-1)
        b = a*a*2
        print((a+b)%MOD)
    
        
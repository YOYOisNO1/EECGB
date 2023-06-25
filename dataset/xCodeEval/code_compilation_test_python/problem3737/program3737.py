def program3737():
    '''den = [1]
    num = [1]
    n = int(input())
    for i in range(n):
        num.append(3*num[-1] + den[-1]-num[-1])
        den.append(4*den[-1])
        
    print num
    print den'''
    
    MOD = 1000000007
    n = int(input())
    if n == 0:
        print 1
        
    else:
        #print ((1<<(n-1)) * (1+ (1<<n)))%MOD
        #print (2**(n-1) * (1+2**n)) %MOD
        z = 1<<(n-1)
        print (z + (z<<(n))) %MOD
        #print ((1<<(n-1)) + (1<<(2*n-1))) %MOD
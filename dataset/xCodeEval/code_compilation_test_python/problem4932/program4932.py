    n_and_c=input().split(' ')
    n=int(n_and_c[0])
    c=int(n_and_c[1])
    
def factorial_modulo(n, d):
        count=1
        i=1
        while i<=n:
            count*=i
            count = count % d
            i+=1
        return count
    
    f = factorial_modulo(n+c, 10**6+3)
    pre_f1 = factorial_modulo(n, 10**6+3)
    f1 = pow(pre_f1, 10**6+1, 10**6+3)
    pre_f2 = factorial_modulo(c, 10**6+3)
    f2 = pow(pre_f2, 10**6+1, 10**6+3)
    
    
    print f*f1*f2 % (10**6+3) - 1
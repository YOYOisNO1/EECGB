def program3516():
    import fractions
    
    x = input()
    
    a = int(x.split(' ')[0])
    b = int(x.split(' ')[1])
    n = int(x.split(' ')[2])
    
    ans = 0
    
    while(n>0):
        n = n - fractions.gcd(a,n)
        if(n<=0):
            ans = 0
        else:
            n = n - fractions.gcd(b,n)
            ans = 1
    
    print(ans)
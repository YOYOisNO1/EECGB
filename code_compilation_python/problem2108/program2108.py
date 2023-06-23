def program2108():
    s  = input().split()
    a = int(s[0])
    b = int(s[1])
    while(a!=0 and b!=0):
        if a>=2*b:
            a=a-2*b
            if b<2*a:
                break
        else:
            b=b-2*a
    
    print('{} {}'.format(a, b)
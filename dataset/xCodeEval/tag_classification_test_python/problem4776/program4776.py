def program4776():
    I=lambda:map(int,input().split())
    n=input()
    a=sorted(list(set(I())))
    
    for i in xrange(len(a)-1):
        if a[i]*2>a[i+1]: print('YES'); exit()
    print('NO')
def program1694():
    a, b = input().split()
    n=int(input())
    if a=='^':
        a1=1
    elif a=='<':
        a1=2
    elif a=='v':
        a1=3
    elif a=='>':
        a1=4
    if b=='^':
        b1=1
    elif b=='<':
        b1=2
    elif b=='v':
        b1=3
    elif b=='>':
        b1=4 
    n=n%4
    a2=a1-n
    a3=a1+n
    if a2<=0:
        a2=a2+4
    if a3>4:
        a3=a3-4
    if (b1==a2)&(b1!=a3):
        print 'cw'
    elif (b1!=a2)&(b1==a3):
        print 'ccw'
    else:
        print 'undefined'
def program4780():
    import sys
    n=input()
    r=map(int,input().split())
    a=[f for f in sorted(set(r))]
    for i in xrange(len(a)-1):
        if 2*a[i]>a[i+1]:
            print('YES')
            sys.exit()
    print('NO')
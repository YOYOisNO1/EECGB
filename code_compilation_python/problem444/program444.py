def program444():
    n1,n2=map(int,input().split())
    c=0
    if (n1==1 and n2==1)
        print 0
    else:
        while n1 > 0 and n2 > 0:
            c = c + 1
            if (n1 < n2) or n1 == n2:
                n1 = n1 + 1
                n2 = n2 - 2
            else:
                n1 = n1 - 2
                n2 = n2 + 1
        print c
    
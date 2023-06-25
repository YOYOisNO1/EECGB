def program1677():
    n,m = map(int,input().split())
    c=0
    for i in xrange(n+1):
        for j in xrange(m+1):
            if i*i +j ==n and i + j*j ==m:
                c+=1
    print(c)
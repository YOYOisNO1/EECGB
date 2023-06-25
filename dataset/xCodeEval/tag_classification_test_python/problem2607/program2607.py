def program2607():
    I=lambda:map(int,input().split())
    p=input()
    cnt=0
    for x in xrange(1,p):
        z=x
        for i in xrange(1,p-1):
            if (z-1)%p==0:
                break
            z*=x
            z%=p
        else:
            if (z-1)%p==0:
                cnt+=1
    print(cnt)
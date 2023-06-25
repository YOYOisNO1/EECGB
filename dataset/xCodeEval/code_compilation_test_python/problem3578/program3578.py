def program3578():
    a,b,w,x,c=map(int,input().split())
    total=0
    while c>a:
       # print b,c,a,total
        if b>=x:
            n=(b/x)
            if n> (c-a):
                n= (c-a)
            c-=n
            b-=n*x
            total+=n
        else:
            c-=1
            a-=1
            b=w-(x-b)
            total+=1
    print total
            
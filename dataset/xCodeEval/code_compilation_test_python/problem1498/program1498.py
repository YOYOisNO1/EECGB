def program1498():
    p,k=map(int,input().split())
    if p<k:
        print(1)
        print(p)
    else:
        f=1
        t=0
        ms=0
        a=[]
        while p+ms*k>=k or p+ms*k<0:
            if t%2==0:
                while p+ms*k>=k:
                    ms-=1
            else:
                while p+ms*k<0:
                    ms+=1
            a.append(p+ms*k)
            t+=1
            p=ms
            ms=0
        print(len(a)+1)
        for i in a:
            print(i,end=' ')
        print(1)
    
def program4470():
    import sys
    m,n=map(int,input().split())
    x=min(m,n)
    y=max(m,n)
    t=0
    if y==1 or y==0:
        print(t)
        sys.exit(0)
    while(x!=0 and y!=0):
        if y%2==0 and y>2:
            p=(y-2)/2
            x+=p
            t+=p
            y=2
        elif y%2!=0 and y>1:
            p=(y-1)/2
            x+=p
            t+=p
            y=1
        elif y==2 or y==1:
            t+=1
            break
        if x>y:
            tmp=x
            x=y
            y=tmp
        #print(x,y)
    print(t)
def program2383():
    a,b = map(int,input().split())
    if a<0 and b<0:
        print a+b,0,0,a+a
    elif a>0 and b>0 :
        print 0,a+b,a+b,0
    elif a<0 ana b>0:
        print a-b,0,0,b-a
    else:
        print 0,b-a,a-b,0
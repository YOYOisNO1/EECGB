def program711():
    n,m,k=map(int,input().split())
    lst=map(int,input().split())
    lst.sort(lambda a,b:b-a)
    need=0
    for i in lst:
        if m<=0 || need>k:break;
        m=m-i+1;need+=1
    
    if need>k || m>0:
        print -1
    else:
        print need
        
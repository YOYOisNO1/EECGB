def program605():
    import sys
    a=list(map(int,input().split()))
    p=a[0]*a[1]
    q=a[2]*a[2]
    if a[2]==1  :
        print(a[1]*a[0])
        sys.exit()
    if p>q :
     if a[1]%a[2]!=0:
            b=int((a[1]/a[2]))+1
     else:
            b=int((a[1]/a[2]))
     if a[0]%a[2]!=0:
            c=int((a[0]/a[2]))+1
     else:
            c=int((a[0]/a[2]))
    print(b*c)
    
    else:
        print(1)
        
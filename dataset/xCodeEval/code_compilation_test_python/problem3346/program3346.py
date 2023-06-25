def program3346():
    [x,y]=[int(i) for i in input().split()]
    s=input()
    pos=[(0,0)]
    j=0
    for i in s:
        if i=='U':
            pos.append((pos[j][0],pos[j][1]+1))
            j+=1
        if i=='D':
            pos.append((pos[j][0],pos[j][1]-1))
            j+=1
        if i=='L':
            pos.append((pos[j][0]-1,pos[j][1]))
            j+=1
        if i=='R':
            pos.append((pos[j][0]+1,pos[j][1]))
            j+=1
    if (x,y) in pos:
        print "Yes"
    else:
        try:
            j=x/pos[-1][0]
        except ZeroDivisionError:
            j=0
        try:
            i=y/pos[-1][1]
        except ZeroDivisionError:
            i=0
        x1=x-(j*pos[-1][0])
        y1=y-(j*pos[-1][1])
        x2=x-(i*pos[-1][0])
        y2=y-(i*pos[-1][1])
        (x3,y3)=(x1,y1)-pos[-1]
        (x4,y4)=(x1,y1)+pos[-1]
        (x5,y5)=(x2,y2)-pos[-1]
        (x6,y6)=(x2,y2)+pos[-1]
        if (x1,y1) in pos or (x2,y2) in pos or (x3,y3) in pos or (x4,y4) in pos or (x5,y5) in pos or (x6,y6) in pos :
            print "Yes"
        else:
            print "No"
    ##[r,g,b]=[int(i) for i in input().split()]
    ##mini=min([r,g,b])
    ##mix=mini-(mini/3)
    ##a=[]
    ##for i in [r,g,b]:   
    ##    rb=(r-i)/3
    ##    bb=(b-i)/3
    ##    gb=(g-i)/3
    ##    a.append(i+rb+bb+gb)
    ##a.append(r/3 + b/3 +g/3)
    ###print(a)
    ##print max(a)
    ####
    ######[n,m]=[int(i)  for i in input().split()]
    ######print m+n-1
    ######for i in range(m):
    ######    print 1,i+1
    ######for i in range(1,n):
    ######    print i+1,1
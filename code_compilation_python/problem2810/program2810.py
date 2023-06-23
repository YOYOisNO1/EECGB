def program2810():
    a=input().split()
    b=input().split()
    y1= int(a[0])
    x1= int(a[1])
    y2= int(b[0])
    x2= int(b[1])
    # 0 = puro par
    # 1= puro impar
    # 2= ambos
    t1=2
    t2=50
    if (x1 %2==0 and y1%2==0):
        t1=0
    elif (x1%2!=0 and y1%2==0):
        t1=1
    if (x2 %2==0 and y2%2==0):
        t2=0
    elif (x2%2!=0 and y2%2==0):
        t2=1
    if ((t1==0 and t2==1) or (t1==1 and t2==0)):
        print -1
    else:
        con=0
    
        while (True):
            #print "dasdas"
            hp = ((y1*con)+x1)
            if((hp-x2)=>0 and (hp-x2)%y2==0):
                print hp
                break
            if (con>10000):
                print -1
                break
            con+=1
def program170():
    a= input().split()
    b=list(set(a))
    l=len(b)
    if l>3:
        print("Alien")
    elif l==1:
        print("Elephant")
    elif l==2:
        i0=a.count(b[0])
        i1=a.count(b[1])
        if i0<4 and i1<4:
            print("Alien")
        elif i0==5 or i1==5:
            print("Bear")
        else:
            print("Elephant")
    else:
        i0=a.count(b[0])
        i1=a.count(b[1])
        i2=a.count(b[2])
        if max(i0,i1,i2)!=4:
            print("Alien")
        else:
            print("Bear")
def program1187():
    l,r,a=input().split()
    l,r,a=[int(l),int(r),int(a)]
    if(l==0 and a==0):
        print(0)
    elif(r==0 and a==0):
        print(0)
    elif(l>r):
        x=l-r
        if(x>=a):
            print((a+r)*2)
        else:
            y=a-x
            print((l+int(y/2))*2)
    elif(r>l):
        x=r-l
        if(x>=a):
            print((a+l)*2)
        else:
            y=a-x
            print((r+int(y/2))*2)
    else:
        print((l+int(a/2))*2)
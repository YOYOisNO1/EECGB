def program556():
    y,b,r=[int(i) for i in input().split()]
    x=[y,b,r]
    if y<b<r:
        print((3*r)+3)
    elif y=r=b:
        print((3*r)-3)
    elif min(x)==r:
        print((3*r)-3)
    elif min(x)==b and b!=r:
        print((3*b))
    elif min(x)==y and y!=r and y!=b:
        if b>r:
            if r-y<=2:
                print((3*r)-3)
            else:
                print((3*y)+3)
        elif b==r:
            if r-y==1:
                print((3*r)-3)
            elif (r-y)>1:
                print((3*y)+3)
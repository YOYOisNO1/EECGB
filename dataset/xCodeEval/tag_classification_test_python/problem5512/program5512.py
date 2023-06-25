def program5512():
    a,x,y=map(int,input().split())
    if y>2*a:
        y1=y-2*a
        no_a=y1//a
        if y1%a==0:
            print(-1)
        else:
            if no_a%2==0:
                left=3+(no_a//2)*3
                if x>0 and x<a:
                    print(left+1)
                elif x<0 and x>-a:
                    print(left)
                else:
                    print(-1)
            else:
                centre=3+((no_a-1)//2)*3+2
                if x<a/2 and x>-a/2:
                    print(centre)
                else:
                    print(-1)
    else:
        if y>a and y<2*a:
            if x>-a/2 and x<a/2:
                print(2)
            else:
                print(-1)
        elif y>0 and y<a:
            if x>-a/2 and x<a/2:
                print(1)
            else:
                print(-1)
        else:
            print(-1)
            
                    
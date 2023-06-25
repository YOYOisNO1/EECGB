def program2588():
    x,y=map(int,input().split())
    if x>y:
        print(x-y)
    else:
        c=0
        while y>x:
            if y%2==0:
                y=y//2
                c+=1
            else:
                y=y+1
                c+=1
        print(c+(x-y))
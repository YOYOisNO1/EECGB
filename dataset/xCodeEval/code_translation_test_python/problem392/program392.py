def program392():
    a,b,c=map(int,input().split())
    if (a==b):
        print("YES")
    elif c!=0:
        if (b-a)%c==0 and (b-a)//c>0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
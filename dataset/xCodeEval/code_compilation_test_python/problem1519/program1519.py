def program1519():
        x,y=(map(int,input().split()))
        a,b=(map(int,input().split()))
        if x==y==a==b==0:
            print(0)
        elif x==y==a==b==1:
            print(2)
        else:
            print(1)
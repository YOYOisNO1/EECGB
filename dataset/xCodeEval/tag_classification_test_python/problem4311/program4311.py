def program4311():
    # cook your dish here
    r=int(input())
    if r==1:
        print("NO")
    else:
        if r%2!=0:
            x=1
            y=(r-3)//2
            if x>=1 and y>=1: 
                print(x,y)
            else:
                print("NO")
        else:
            print("NO")
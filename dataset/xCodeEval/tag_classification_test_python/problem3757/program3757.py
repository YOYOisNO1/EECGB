def program3757():
    x, y = map(int, input().split())
    if y==1 and x==0:
        print("yes")
    elif y==0 and x==1:
        print("no")
    elif x%2==0 and y%2==1 and x>=y-1 and y>1 or x%2==1 and y%2==0 and x>=y-1 and y>1:
        print("yes")
    else:
        print("no")
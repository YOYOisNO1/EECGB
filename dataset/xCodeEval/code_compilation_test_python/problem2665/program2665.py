def program2665():
    x,y=list(map(int,input().split()))
    c=0
    if y==0 and (x==0 or x==1):
        c=0
    elif abs(x)==abs(y) and x>0 and y>0:
        c=4*x-3
    elif abs(x)==abs(y) and x<0 and y>0:
        c=4*y-2
    elif abs(x)==abs(y) and x<0 and y<0:
        c=-4*x-1
    elif abs(x)==abs(y) and x>0 and y<0
    elif x>0 and y<0 and y==-(x-1):
        c=-4*y
    elif x>y and abs(x)>abs(y):
        c=4*x-3
    elif y>x and abs(y)>abs(x):
        c=4*y-2
    elif y>x and abs(x)>abs(y):
        c=-4*x-1
    elif x>y and abs(x)<abs(y):
        c=-4*y
        
    print(c)
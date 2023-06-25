def program663():
    a=int(input())
    b=int(input())
    if a>b:
        k=a-b
    else
        k=b-a
    if k%2==0:
        j=k//2
        x=0
        for v in range(0,j+1):
            x=x+v
        y=0
        for v in range(j,0,-1):
            y=y+v
        print(x+y)
    else:
        j=(k//2)
        x=0
        for s in range(0,j+1):
            x=x+s
        y=0
        for s in range(j+1,0,-1):
            y=y+s
        print(x+y)
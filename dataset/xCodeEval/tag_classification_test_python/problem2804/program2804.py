def program2804():
    #CF401 yl1
    n=(int(input()))%6
    x=int(input())
    for i in range(n,0,-1):
        if i%2==1:
            if x==0:    x=1
            elif x==1:  x=0
            else:       x=2
        else:
            if x==0:    x=0
            elif x==1:  x=2
            else:       x=1
    print(x)
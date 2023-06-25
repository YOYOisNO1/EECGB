def program3801():
    X,x=map(int,input().split())
    a=[int(i) for i in input().split()]
    a=a[::-1]
    h=0
    for i in range(X):
        h+=a[i]*x**i
    Y,y=map(int,input().split())
    b=[int(i) for i in input().split()]
    b=b[::-1]
    k=0
    for i in range(Y):
        k+=b[i]*y**i
    if(h==k):
        print('=')
    elif(h<k):
        print('<')
    else:
        print('>')
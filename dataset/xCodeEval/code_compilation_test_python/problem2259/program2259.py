def program2259():
    a,b=[int(i) for i in input().split()]
    x,y,z=[int(i) for i in input().split()]
    p=2*x+y
    q=3*z+y
    if p>a and q>b :
        print(p-a+q-b)
    elif p>a :
        print(p-a)
    elif :
        print(q-b)
    else :
        print('0')
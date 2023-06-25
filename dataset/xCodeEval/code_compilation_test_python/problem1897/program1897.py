def program1897():
    from math import sqrt
    n=int(input())
    x=[]
    y=[]
    sumo=0
    i=0
    f=0
    while(f==0 ):
        i=i+1
        ln=n
        n=n-i
        y.append(i)
        if(n in y):
            break
        else:
            x.append(i)
    x.append(ln)
    print(len(x))
    for i in x:
        print(i,end=' ')
        
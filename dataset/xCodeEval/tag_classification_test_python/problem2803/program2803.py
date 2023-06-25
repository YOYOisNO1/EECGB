def nap(y):
        if y==0:
            p=[0,1,2]
            return p
        if y==1:
            p=[1,0,2]
            return p
        if y==2:
            p=[1,2,0]
            return p
        if y==3:
            p=[2,1,0]
            return p
        if y==4:
            p=[2,0,1]
            return p
        if y==5:
            p=[0,2,1]
            return p
    n=int(input())
    x=int(input())
    n=n%6
    m=nap(n)
    print(m[x])
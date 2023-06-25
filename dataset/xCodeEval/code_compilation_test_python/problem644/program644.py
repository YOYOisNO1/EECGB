def program644():
    n,a,b,c=input().split(" ")
    n=int(n)
    a=int(a)
    b=int(b)
    c=int(c)
    if(n%4==0):
        print(0)
    else :
        n=n%4
        b=b/2
        c=c/3
        n=4-n
        if(n==3):
            a=min(a,c)
            print(int(a*n))
        elif(n==1)
            print(int(a * n))
        else:
            a = min(a, b)
            print(int(a * n))
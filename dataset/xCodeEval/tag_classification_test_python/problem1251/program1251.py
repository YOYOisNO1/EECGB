def program1251():
    n=int(input())
    a=list(input())
    f=0
    x=0
    for i in range (n):
        if a[i]=="-":
            x-=1
            if f>x:
                f=x
        else:
            x+=1
    print((x-f))
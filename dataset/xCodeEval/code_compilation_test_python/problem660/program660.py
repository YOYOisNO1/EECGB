def program660():
    a,b=(int(i) for in input().split())
    if b>a & b%a==0:
        c=b//a
        print(((c-a)(c-a+1)/2) +((b-c)(b-c+1)/2))
    elif b%a!=0:
        d=(b//a)+0.5
        print(((d-a)(d-a+1)/2)+((b-d)(b-d+1)/2))
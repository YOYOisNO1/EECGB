def program3350():
    n=int(input())
    a=int(input())
    b=int(input())
    c=int(input())
    mi=min(a,b,c)
    ma=max(a,b,c)
    if n==1:
        print(0)
    elif mi==a or mi==b:
        print((n-1)*mi)
    else:
        print((a+b+c)-mi-ma + (n-2)*mi)
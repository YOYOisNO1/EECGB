def program6318():
    a,b=map(int,input().split())
    a+=1
    b=min(b,a+11)
    d=1
    while a<=b:
        d*=a%10
        a+=1
    print(d%10)
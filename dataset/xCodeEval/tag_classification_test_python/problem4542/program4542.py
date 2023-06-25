def program4542():
    x=input()
    a,b=map(int,input().split())
    f=0
    y=0
    while True:
        if a%10==7 or a/10==7 or b%10==7 or b/10==7:
            print(y)
           # print(a,b)
            break
        b-=x
        y+=1
        if b<0:
            a-=1
            b+=60
        if a<0:
            a+=24
        
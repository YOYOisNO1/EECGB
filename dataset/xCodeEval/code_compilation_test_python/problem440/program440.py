def program440():
    a,b=map(int,input().split())
    p=0
    if a==1 and b==1:
            p=0
    else:
        while 1:
            elif a!=0 and b!=0 and a<=b:
                a+=1
                b-=2
                p+=1
            elif a!=0 and b!=0 and b<a:
                b+=1
                a-=2
                p+=1
            elif a==0 or b==0:
                break
    print(p)
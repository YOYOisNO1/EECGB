def program443():
    a1,a2=map(int,input().split())
    if(a1<a2):
        a1+=1
        a2-=2
        x=1
    else:
        a2+=1
        a1-=2
        x=2
    h=1
    while True:
        if(a1==2 and x==2):
            x=1
        elif(a2==2 and x==1):
            x=2
        if(x==1):
            a1+=1
            a2-=2
        else:
            a2+=1
            a1-=2
        h+=1
        if(a1<=0 or a2<=0):
            break
        elif(a1==1 and x==2):
            x=1
        elif(a2==1 and x==1):
            x=2
    print(h
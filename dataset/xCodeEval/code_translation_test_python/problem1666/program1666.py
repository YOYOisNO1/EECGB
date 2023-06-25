def program1666():
    a,b = map(int,input().split())
    a,b = min(a,b),max(a,b)
    if a==1:
        c=b%6
        if c==4:print((b//6)*6 + 2)
        elif c==5:print((b//6)*6 + 4)
        else:print((b//6)*6)
    elif a==2:
        if b<=2:print(0)
        elif b==3 or b==7:print((a*b)-2)
        else:
            print((b) * 2)
    else:
        ans=a*b
        if ans%2==0:
            print(ans)
        else:
            print(ans-1)
    
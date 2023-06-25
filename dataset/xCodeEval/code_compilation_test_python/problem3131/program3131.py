def program3131():
    n=int(input())
    if n==3:
        print("24")
    elif n==4:
        print("132")
    else:
        cap=(2n-2)
        ans=2*(12*pow(4,(n-3)))
        tmp=n-4
        if tmp>=0:
            ans+=tmp*(36*pow(4,tmp))
        print(ans)
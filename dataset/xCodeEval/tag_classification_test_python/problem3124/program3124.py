def program3124():
    m,s=input().split()
    m=int(m)
    s=int(s)
    l1=0
    l2=0
    if s==0:
        if m>1:
            l1-=1
            l2-=1
        elif m==1:
            l1=0
            l2=0
    else:
        if 9*m<s:
            l1-=1
            l2-=1
        elif s==(9*m):
            l1=l2=10**m-1
        else:
            if s>9:
                t=int(s/9)
                if m<=2:
                    l1+=(s-9*t)*(10**(m-1))
                    for i in range(1,t+1):
                        l1+=9*(10**(i-1))
                else:
                    l1+=10**(m-1)
                    l1+=10**t-1
                    if s>9*t:
                        l1+=(s-9*t-1)*(10**t)
                    else:
                        l1-=10**(t-1)
                l2+=(s-9*t)*(10**(m-t-1))
                for i in range(1,t+1):
                    l2+=9*(10**(m-i))
            else:
                l1=10**(m-1)+s-1
                l2=s*(10**(m-1))
    print('%s %d'%(l1,l2))
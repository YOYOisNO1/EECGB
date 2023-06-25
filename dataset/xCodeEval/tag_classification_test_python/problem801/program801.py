def program801():
    ch=input()
    n=int(input())
    l=[int(ch[:2]),int(ch[3:])]
    m=l[1]+n
    h=(l[0]+(m//60))%24
    m=m%60
    if (h //10)==0:
        print(0,end='')
    print(h,end=':')
    if (m//10)==0:
        print(0,end='')
    print(m)
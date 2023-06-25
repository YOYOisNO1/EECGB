def program4655():
    import sys
    n,k=map(int,input().split())
    s=input()
    start={}
    close={}
    for i in range(n):
        kk=s[i]
        try:
            a=start[kk]
            close[kk]=i
        except KeyError:
            start[kk]=i
            close[kk]=i
    ac=0
    for i in range(n):
        kk=s[i]
        if(start[kk]==i):
            ac+=1
            if(ac>k):
                print("YES")
                sys.exit(0)
        if(close[kk]==i):
            ac-=1
        if(ac>k):
            print("YES")
            sys.exit(0)
    print("NO")
    
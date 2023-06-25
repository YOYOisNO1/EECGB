def program734():
    import sys
    a,b,c=map(int,input().split())
    c=c%b
    # print(a)
    for x in range(1,15000000000):
        if(x*a>10000):break
        elif ((x*a)%b==c):
            print("Yes")
            sys.exit()
    print("No")v
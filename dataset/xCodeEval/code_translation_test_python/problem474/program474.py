def program474():
    a,b,c,d=map(int,input().split())
    tot=a+b-c
    if c>b or c>a:
            print(-1)
            exit()
    if tot>d-1:
            print(-1)
            exit()
    print(d-tot)
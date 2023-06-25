def program4050():
    #!/usr/bin/python3.5
    n=int(input())
    if n==1:
        print(-1)
        quit()
    if n==2:
        a,b=[int(x) for x in input().split()]
        c,d=[int(x) for x in input().split()]
        if a!=c and b!=d:
            print(abs(a-c)*abs(b-d))
            quit()
        else:
            print(-1)
            quit()
    if n==3:
        a,b=[int(x) for x in input().split()]
        c,d=[int(x) for x in input().split()]
        e,f=[int(x) for x in input().split()]
        k=[abs(a-c),abs(a-e)]
        l=[abs(b-d),abs(b-f)]
        print(max(k)*max(l))
        quit()
    a,b=[int(x) for x in input().split()]
    c,d=[int(x) for x in input().split()]
    e,f=[int(x) for x in input().split()]
    g,h=[int(x) for x in input().split()]
    k=[abs(a-c),abs(a-e)]
    l=[abs(b-d),abs(b-f)]
    print(max(k)*max(l))
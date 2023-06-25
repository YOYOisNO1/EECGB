def program181():
    w=int(input())
    n=int(input())
    s=0
    for i in range(0,n):
        f=input()
        z=f.split( )
        s=s+(int(z[0])*int(z[1]))
    g=int(s/w)
    print(g)
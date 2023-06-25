def program1082():
    from sys import stdout,stdin
    n=int(stdin.readline())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    v=min(a[0],b[1])+min(a[1],b[2])+min(a[2],b[0]);u=n-(min(b[0],a[0]+a[1])+min(b[1],a[1]+a[2])+min(b[2],a[2]+a[0]))
    stdout.write(str(u)+' '+str(v)) 
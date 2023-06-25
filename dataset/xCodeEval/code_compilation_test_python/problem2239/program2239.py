def program2239():
    n,m=map(int,input().strip().split())
    l=[int(i) for i in range(1,n+1) if i%2!=0]
    e=[int(i) for i in range(1,n+1) if i%2==0]
    if(n%2==0):
        if(m>n//2):
            print(e[m-(n//2)-1])
        else:
            print(l[m-1])
    else:
        if(m>(n//2)+1):
            print(e[m-2-(n//2))
        else:
            print(l[m-1])
            
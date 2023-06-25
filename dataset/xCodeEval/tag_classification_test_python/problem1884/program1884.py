def program1884():
    n,m=map(int,input().split())
    if(n%2==0):
        if(m>n//2):
            print((m-(n//2))*2)
        else:
            print((m*2)-1)
    else:
        if(m>(n//2)+1):
            print((m-((n//2)+1))*2)
        else:
            print((m*2)-1)
def program2331():
    a,b,c=map(int,input().split())
    d,e,f=map(int,input().split())
    g,h,i=map(int,input().split())
    u=(d+f)//2
    su=d+u+f
    print(su-(b+c),b,c)
    print(d,u,f)
    print(g,h,su-(g+h))
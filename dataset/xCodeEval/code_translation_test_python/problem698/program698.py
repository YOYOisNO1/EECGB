def program698():
    l=list(map(int,input().split()))
    ka=sum(l)
    if(ka==0 or ka%5!=0):
        print(-1)
    else:
        print(ka//5)
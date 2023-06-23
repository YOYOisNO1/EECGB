def program412():
    x,y = map(int,input().split())
    if(x<y): print(-1)
    else:
        c=(x//2)%y
        if(!c): c=y-c
        print(x//2+c)
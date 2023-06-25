def program3318():
    a=list(map(int,input().split()));b=max(a)
    a.remove(b);print(max(0,b+1-a[0]-a[1]))
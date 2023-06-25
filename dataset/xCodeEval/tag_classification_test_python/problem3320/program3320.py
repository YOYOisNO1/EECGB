def program3320():
    a=list(sorted(map(int,input().split())))
    print(max(0,a[2]+1-a[0]-a[1]))
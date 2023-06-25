def program1024():
    n=input()
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    maxx=0
    minn=0
    maxx+=min(a[0],b[1])+min(a[1],b[2])+min(a[2],b[0])
    minn+=max(0,a[0]-b[0]-b[2])+max(0,a[1]-b[1]-b[0])+max(0,a[2]-b[1]-b[2])
    print(minn,maxx)
    
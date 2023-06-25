def program1101():
    n=int(input())
    a=[int(e) for e in input().split()]
    b=[int(e) for e in input().split()]
    minw=0
    if a[0]>b[0]+b[2]:
        minw+=a[0]-b[0]-b[2]
    if a[1]>b[0]+b[1]:
        minw+=a[1]-b[0]-b[1]
    if a[2]>b[1]+b[2]:
        minw+=a[2]-b[1]-b[2]    
    maxw=min(a[0],b[1])+min(a[2],b[0])+min(a[1],b[2])
    print(minw,maxw)
    
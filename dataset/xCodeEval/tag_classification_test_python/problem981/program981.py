def program981():
    n=int(input(''))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
     
    mxsol=min(a[0],b[1])+min(a[1],b[2])+min(a[2],b[0])
    mnsol=max(0,a[0]-b[0]-b[2],a[1]-b[1]-b[0],a[2]-b[2]-b[1])
    print(mnsol,mxsol)
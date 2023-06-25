def program1032():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    mx = 0
    mn = 0
    mx = min(a[0],b[1]) + min(a[1],b[2]) + min(a[2],b[0])
    mn = max(0,a[0]-b[0]-b[2]) + max(0,a[1]-b[1]-b[0]) + max(0,a[2]-b[2]-b[1])
    print(mn,mx)
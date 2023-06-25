def program1069():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    
    mx = min(a[0],b[1]) + min(a[1],b[2]) + min(a[2],b[0])
    mn = max(a[0]-b[0]-b[2],a[1]-b[1]-b[0],a[2]-b[2]-b[1],0)
    print(mn,mx)
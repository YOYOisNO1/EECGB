def program2113():
    n = int(input())
    ar = map(int,input().split())
    temp = ar.count(1)
    if temp==n:
        print n-1
    else:
        cnt1,cnt0,z=0,0,0
    
        for i in range(n):
            if ar[i]==1:
                cnt1 += 1
                z = max(z-1,0)
            else:
                z += 1
            cnt0 = max(cnt0,z)
        print cnt0+cnt1n = int(input())
    ar = map(int,input().split())
    
    cnt1,cnt0,z=0,0,0
    
    for i in range(n):
        if ar[i]==1:
            cnt1 += 1
            z = max(z-1,0)
        else:
            z += 1
        cnt0 = max(cnt0,z)
    print cnt0+cnt1
def check(mid , lis):
        pile=[10000000000]*mid
        c=0
        for i in range(n-1,-1,-1):
            pile[i%mid]=min(pile[i%mid]-1,lis[i])
    #    print(pile,mid)    
        if min(pile)<0:
            return 0
        else:
            return 1    
    n = int(input())
    lis = sorted(map(int,input().split()))
    l=1
    r=n
    while l<=r:
        mid = l + (r-l)//2
    #    print(l,r,mid)
        if(check(mid,lis)):
            r = mid-1
        else:
            l = mid+1
    print(l)            
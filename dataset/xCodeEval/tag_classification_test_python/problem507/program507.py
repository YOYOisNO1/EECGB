def ch(x):
        num=x
        while x>0: num+=x/k;x=x/k
        return num>=n
    n, k=map(int,input().split())
    left=1
    right=n
    mid=0
    while left<=right :
        mid=(left+right)/2
        if ch(mid): right=mid-1
        else : left=mid+1
    print(left)
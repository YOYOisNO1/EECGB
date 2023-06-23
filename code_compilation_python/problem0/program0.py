def binarysearch(sequence, value):
        lo, hi ,mid= 0, 1000,0
        while lo < hi:
    
            mid=(lo+hi)//2
    
            if sequence[mid]<=value and sequence[mid+1]>value:
                return a[mid]
            elif sequence[mid]>value:
                hi=mid
            elif sequence[mid]<value:
                lo=mid
    
        return a[mid]
    n=int(input())
    a=[i**2 for i in range(1,1001)]
    
    used=binarysearch(a,n)
    left=n-used
    side=int(used**(0.5))
    ans=4*side
    if  left and left>side:
        print(ans+4)
    elif left:
        print(ans+2)
    else:
        print(ans)
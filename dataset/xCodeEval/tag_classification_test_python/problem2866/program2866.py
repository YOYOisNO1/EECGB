def program2866():
    n,x,pos=list(map(int,input().split()))
    max=(7+1e9)
    rem=1
    start=0
    end=n
    left_value=x-1
    right_value=n-x
    while start<end:
        mid=(start+end)//2
        if mid>pos:
            rem=(rem*right_value)%max
            right_value-=1
            n-=1
            end=mid
        elif mid<pos:
            rem=(rem*left_value)%max
            left_value-=1
            n-=1
            start=mid+1
        else:
            start=mid+1
    
    
    for i in range(1,n):
        rem=(rem*i)%max
    rem=rem%max
    print(int(rem))
    
def program2585():
    n,m=map(int,input().split());c=0
    while m>n:
        if m%2==0:m//=2
        else:m+=1
        c+=1
    if m<n:c+=n-m
    print(c)
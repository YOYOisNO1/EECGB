def program998():
    n,a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    l=0
    if b[a-1]==1:
        l=1
    else:
        l=0
    i,j=a-1,a+1
    while i>=1 or j<=n:
        if i>=1 and j<=n:
            if b[i-1]==b[j-1]==1:
                l+=2
            i--
            j++
        elif i<1:
            l+=1
            j++
        else:
            l+=1
            i--
    print(l)
def program553():
    n,m,k=map(int,input().split())
    if m<k:
        if m>=n:
            print('Yes')
        else:
            print('No')
    elif k<m:
        if k>=n:
            print('Yes')
        else:
            print('No')
    elif k==m:
        if k>=n:
            print('Yes')
        else:
            print('No')
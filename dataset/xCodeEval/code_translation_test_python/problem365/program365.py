def program365():
    n,m,k=list(map(int,input().split()))
    if k<n:
        print(str(k+1)+' 1')
    else:
        div,mod = divmod(k-n,m-1)
        if div%2:
            print(str(n-div)+' '+str(m-mod))        
        else:
            print(str(n-div)+' '+str(2+mod))
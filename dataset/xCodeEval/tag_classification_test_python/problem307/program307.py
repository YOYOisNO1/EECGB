def program307():
    n,m,k=map(int, input().split())
    
    if (m+n)%2==1:
        if k==-1:
            print(0)
        else:
            if m*n<m+n:
                print(1)
            else:
                print(pow(2,) (n-1)* (m-1), 1000000007)
    
    
    else:
        print(pow(2,) (n-1)* (m-1), 1000000007)
def program4573():
    n,m,k = map(int,input().split())
    if k < n:
        print(k+1,1)
    else:
        k = k-n
        t1 = k//(m-1)
        t2 = k % (m-1)
        if t1 % 2:
            print(n-t1,m-t2)
        else:
            print(n-t1,2+t2)
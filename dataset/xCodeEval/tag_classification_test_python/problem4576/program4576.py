def program4576():
    n,m,k = map(int,input().split())
    x = n
    if n>k:
        print(k+1,1)
        exit(0)
    k -= n
    m-=1
    x-=2*(k//(2*m))
    k%=2*m
    
    if x==0:
        print(1,2)
        exit(0)
    if k<m:
        print(x,k+2)
    else:
        k-=m;
        print(x-1,m+1-k)
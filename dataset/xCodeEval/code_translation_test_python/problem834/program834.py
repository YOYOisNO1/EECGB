def program834():
    n,k,m,q=map(int,input().split())
    print(max(i*min(m,n//(k*i-k+1))for i in range(1,q+1)))
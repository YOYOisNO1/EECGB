def program983():
    n1=int(input())
    x,y,z=map(int,input().strip().split())
    m,n,o=map(int,input().strip().split())
    a=min(x,n)+min(y,o)+min(z,m)
    b=min(n1-n,x)+min(n1-m,z)+min(n1-o,y)
    j=n1-b
    if j<0:j=0
    print(j,a) 
def program3417():
    n,m=set(map(int,input().split()))
    print(n*m-(min(m%6,6-m%6) if n==1 else 2*(m in [3,7])+4*(m==2) if n==2 else n&1*m&1))
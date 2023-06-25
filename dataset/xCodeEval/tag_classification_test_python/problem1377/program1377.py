def program1377():
    n,m=map(int,input().split())
    print(m*(n/m)*(n/m-1)/2+(n/m)*(n%m),(n-m)*(n-m+1)/2)
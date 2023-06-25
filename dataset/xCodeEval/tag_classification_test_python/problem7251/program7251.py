def program7251():
    n,m = map(int,input().split())
    if(n==1 and m==1):
        print("1.0")
    else:
        print(float((1) + (float((n-1)*(m-1))/float(m*n-1))))/float(n);
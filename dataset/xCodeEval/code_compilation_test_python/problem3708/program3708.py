def program3708():
    M=10**9+7
    x=input()
    n=len(x)
    w,c=0,1
    for i in range(n):
      if '1'==x[i]:
        w=(w+c*pow(2,(n-1-i)*2,M))%M
      print c,pow(2,n-1-i,M)
      c=c*2%M
    print w
def program2547():
    z=input;c,n,k,a,b=0,int(z()),int(z()),int(z()),int(z())
    if k>1:
        while(((n//k)*a*(k-1))>b):c+=(n%k)*a +b;n=n//k
    c+=(n-1)*a;print(c)
def program406():
    n,k,l,c,d,p,nl,np=map(int,input().split())
    print(min(k*l/nl,c*d,p/np)/n)
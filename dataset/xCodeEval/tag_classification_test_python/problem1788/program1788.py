def program1788():
    R=lambda:list(map(int,input().split()))
    k,l=R(); n=R(); m=sorted(R())
    n[n.index(0)]=m[0]
    print(['YES','NO'][l==1 and n==sorted(n)])
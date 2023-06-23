def program610():
    k,n,s,p= map(int, input().split())
    sp=n/s
    spq=round(sp+1)
    r=(spq*k/p)
    if r%1==0:
        print(int(r))
    else:
        print(int(round(r+1))
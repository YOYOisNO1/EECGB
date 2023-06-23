def program612():
    n,s,k,l=list(map(int,input().split()))
    if s//k==s/k: 
        op=int(s//k)
    else:
        op=int(s//k)+1
    kam=n*op
    if kam//l==kam/l:
        print(int(kam/l)
    else:
        print(int(kam//l)+1)
def program2235():
    n, k=map(int,input().split())
    l=[]
    m=[]
    for i in range(1,n+1):
              if(i%2!=0):
                        l.append(i)
    for j in range(2,n+1):
              if(i%2==0):
                        m.append(j)
    x=list(l+m)
    print(x[k]):
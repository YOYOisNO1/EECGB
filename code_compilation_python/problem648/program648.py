def program648():
    l=[]
    p=[]
    n=int(input())
    m=int(input())
    if 2<=n<=m<=50:
       for i in range(m):
           l.append(int(input())
       for i in range(0,m-n+1):
           p.append(l[i+4-1]-l[i])
       print(min(p))
    else:
        print("redo")
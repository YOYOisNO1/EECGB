def program2537():
    p=[]
    n,m=input().split()
    l=[int(x) for x in input().split()]
    l.sort()
    for i in range(0,int(m)-int(n)+1):
       p.append(l[i+int(n)-1]-l[i])
    p.sort()
    print(p[0])
def gh(z,i):
        k=str(z[:i])+str(int(z[i])-1)+'9'*len(z[i+1::])
        return (sum(map(int,k)),k)
    a=input();p=[]
    for i in range(len(a)-1):
        if a[i]!='0':p.append(gh(a,i))
    p.append((sum(map(int,a)),a))
    print(int(sorted(p,reverse=True)[0][1]))
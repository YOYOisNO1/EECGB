def pos(x):
        global m
        global n
        row=x/m
        column=x%m
        p=[row,column]
        return p
    n,m,a,b=(int(i) for i in input().split())
    l=pos(a-1)
    par=l[0]
    pac=l[1]
    l=pos(b-1)
    pbr=l[0]
    pbc=l[1]
    if (par==pbr) or ((pac==0) and (pbc==m-1)) or (pac==0 and b==n):
        print(1)
    elif (pac-pbc==1) or (pac==0) or (pbc==m-1) or (a==1) or (b==n) or (pbr-par==1):
        print(2)
    else:
        print(3)
    #print(par,pac,pbr,pbc)
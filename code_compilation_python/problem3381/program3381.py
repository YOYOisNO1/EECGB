def program3381():
    a=list(map(str,input().split(":")))
    a=list(a[0][0]+a[0][1]+a[1][0]+a[1][1])
    s=0
    while a!=a[::-1]:
        a[3]=str(int(a[3])+1)
        if a[3]=="10":
            a[3]="0"
            a[2]=str(int(a[2])+1)
        if a[2]=="6":
            a[2]="0"
            a[1]=str(int(a[1])+1)
        if a[0]+a[1]=="24":
            a[0],a[1],a[2],a[3]="0","0","0","0"
        s+=1
    print(s)
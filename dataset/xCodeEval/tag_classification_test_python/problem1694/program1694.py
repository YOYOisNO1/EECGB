def program1694():
    n=int(input())
    a=[0]*100
    tool = 1
    a[0]=1
    f = 1
    for i in range(1,n):
        
        a[tool]=1
        tool+=1
        f+=1
        if f==2:
            f=0
            tool-=1
            a[tool-1]=a[tool]+1
            c=0
            for j in range(tool-1,0,-1):
                    if a[j]==a[j-1]:
                        a[j-1]=a[j]+1
                        c+=1
                    else:
                        break
            tool-=c
        else:
            pass
    print(*a[:tool])
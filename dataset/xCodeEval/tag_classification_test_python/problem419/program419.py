def program419():
    n,m = map(int,input().split())
    l =list(map(int,input().split()))
    mark={}
    a=[-1]*(n)
    for i in range(m-1):
        temp=l[i+1]-l[i]
        if l[i+1]-l[i] <=0:
            temp+=n
        if a[l[i]-1]==temp:
            continue
        if a[l[i]-1]==-1:
            a[l[i]-1]+=temp+1
            if a[l[i]-1] not in mark:
                mark[a[l[i]-1]]=1
            else:
                print('-1')
                break
        else:
            print('-1')
            break 
    else:    
        fill=[]
        for i in range(1,n+1):
            if i not in mark:
                fill.append(i)
        c=0
        for i in range(n):
            if c>=n:
                print('-1')
                break
            if a[i]==-1:
                a[i]=fill[c]
                c+=1
        print(*a)
def program2703():
    n,b=map(int,input().split())
    a=list(map(int,input().split()))
    q,w,l,m=0,0,[],0
    for i in range(n-1):
        if a[i]&1:q+=1
        else:w+=1
        if q==w:l.append(abs(a[i]-a[i+1]))
    l.sort()
    for i in l:
        if i<=b:m+=1;b-=i
        else:break
    print(m)
def program2181():
    n,c=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    t1=[0]*n
    t2=[0]*n
    t1[0]=l2[0]
    t2[n-1]=l2[n-1]
    for i in range(1,n):
        t1[i]=l2[i]+t1[i-1]
    for i in range(n-2,-1,-1):
        t2[i]=l2[i]+t2[i+1]
    l=r=0
    for i in range(n):
        l+=max(0,(l1[i]-(c*t1[i])))
    for i in range(n):
        r+=max(0,l1[i]-c*t2[i])
    if(l>r):
        print("Limak")
    elif(l<r):
        print("Radewoosh")
    else:
        print("Tie")
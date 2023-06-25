def program2081():
    n,k,d=map(int,input().split())
    l1=[0]
    for i in range (1,n+1):
        if i<=k:
            l1.append(2**(i-1))
        else:
            l1.append(sum(l1[i-k:i]))
    l2=[0]
    for i in range (1,n+1):
        if i<=d-1:
            l2.append(2**(i-1))
        else:
            l2.append(sum(l2[i-d+1:i]))
    print((l1[n]-l2[n])%(10**9+7))
def program3005():
    n,k,x=map(int,input().split())
    a=list(map(int,input().split()))
    temp=k
    if(len(a))<=2:
        print(k*x)
    else:
        while(k>0):
             a.remove(max(a))
             k=k-1
        print(sum(a)+temp*x)
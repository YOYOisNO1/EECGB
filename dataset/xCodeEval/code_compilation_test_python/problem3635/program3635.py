def program3635():
    from bisect import*
    A=lambda:map(int,input().spilt())
    t,=A()
    for  _ in [0]*t:
        n,k=A();x=sorted(A());A();a=q=0;m=[n-i-bisect_left(x,x[~i]-k)for i in range(n):
        for i in range(n):a=max(a,q+bisect_right(x,x[i]+k-i);q=max(q,m[~i])
        print(a)
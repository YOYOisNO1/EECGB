def check(k,z,n):
        if k==0:
            print(k)
            return
        counter=0
        for i in z:
            counter+=int(z[i]/k)
        if counter>=n:
             print(k)
             return
        else:
            k=k-1
            check(k,z,n)
    n,m  = map(int, input().split())
    from collections import Counter
    qlist=map(int,input().split())
    z=Counter(qlist)
    k=int(m/n)
    check(k,z,n)
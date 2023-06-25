def recur(n,k):
        if k==2**(n-1)-1:
            return n
        elif k>2**(n-1)-1:
            return recur(n-1,k-2**(n-1))
        else:
            return recur(n-1,k)
    n,k=map(int,input().split())
    print(recur(n,k-1))
def program2600():
    # author: ankan2526
    
    import math, bisect, heapq, random
    
    for t in range(int(input())):
        n,m,k=map(int,input().split())
        c=(n*m)//2
        if n%2==m%2==0:
            if k%2:
                print("NO")
            else:
                print("YES")
            continue
        if m%2:
            n,m=m,n
            k=c-k
        if n==1:
            if k<c:
                print("NO")
            else:
                print("YES")
            continue
        x=m//2
        if x%2==k%2 and k>=x:
            print("YES")
        else:
            print("NO")
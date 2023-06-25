def program929():
    n,m=map(int,input().split())
    a=list(map(int,input()split()))
    a.sort()
    s=sum(a)-a[n-1]
    if s>m:
    	print("NO")
    else:
    	print("YES")
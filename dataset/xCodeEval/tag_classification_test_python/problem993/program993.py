def program993():
    n=int(input())
    k1,n1,b1=map(int,input().split())
    k2,n2,b2=map(int,input().split())
    max=min(k1,n2)+min(n1,b2)+min(b1,k2)
    min=min(k1,n-n2)+min(n1,n-b2)+min(b1,n-k2)
    print(n-min,max)
def quantity(x):
        if x < 2:
            return 1
        else:
            return quantity(x // 2) * 2 + 1
        
def z(x,l,r):
        if x==0 or l>r:
            return 0
        if x==1:
            return 1
        k=quantity(x//2)
        if l<=k+1<=r:
            m=x%2
        else:
            m=0
        return z(x//2,l,min(k,r))+m+z(x//2,max(1,l-(k+1)),r-(k+1))
    x,l,r=map(int,input().split())
    print(z(x,l,r))
            
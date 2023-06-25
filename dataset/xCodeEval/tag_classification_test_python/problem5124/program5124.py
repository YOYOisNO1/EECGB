def midof(n):
        i=1
        while i<=n:i<<=1
        return i>>1
def count_one(n,l,r):
        if n<2:return n
        mid = midof(n)
        if l==0 and r==2*mid-1:return n
        if n+1==2*mid: return r-l+1
        c = (n%2)*(l<=mid<=r)
        if l<mid:c+=count_one(n//2,l,r if r<mid else mid-1)
        if r>mid:c+=count_one(n//2,l-mid if l>mid else 1,r-mid)
        return c
    print(count_one(*map(int,input().split())))
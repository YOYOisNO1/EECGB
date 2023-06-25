    from xml.dom import minidom
    
    
def solve():
        arr=list(input().split())
        n,p=int(arr[0]),float(arr[1])
    
    def judge(m):
            res=0
            res+=(m*(n-m)*(n-m-1))/4 
            res+=(m*(max(0,m-1))*(n-m))/2
            res+=m*(max(m-1,0))*(max(m-2,0))/6
            #print('res',m,res)
            return res<p*(n*(n-1)*(n-2)/6)
        
        l,r=0,n
        while l<r:
            mid=(l+r)>>1
            #print(mid)
            if judge(mid):
                l=mid+1
            else:
                r=mid
        
        print(l)
    
    solve()
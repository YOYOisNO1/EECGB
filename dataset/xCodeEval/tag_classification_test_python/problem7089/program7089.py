    
    MAX=10**9+7
def mult_mod(a,b):
        return (a*b)%MAX
    
    p, k=map(int, input().split())
    
def k_not_one():
        visited=[False]*p
    
        res=1
        for i in xrange(1,p):
            if not visited[i]:
                res=mult_mod(res, p)
                current=i
                while(not visited[current]):
                    visited[current]=True
                    current=(current*k)%p
        return res
        
def k_one():
        res=1;
        for _ in xrange(p):
            res=mult_mod(res, p)
        return res
    
    print(k_one()) if k==1 else k_not_one()
    
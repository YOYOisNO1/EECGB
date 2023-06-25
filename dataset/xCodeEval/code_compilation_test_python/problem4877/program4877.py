    # Read input
    n,m,k = map(int,input().split())
    a     = [map(int,input().split())+[i+1] for i in range(m)]
    
def reduce (e,x,y,d,cst):
        return [cst-((cst-max(e[0],x))/(k**d))*k**d,
                cst+((min(e[1],y)-cst)/(k**d))*k**d]
    
    # Recursive approach
def next (s1,s2,cst,d,mi,ma,l,r):
        ll = [reduce(e,mi,ma,d,cst)+[e[2],e[3]] for e in l if ma>=e[0] and mi<=e[1]]
        if len(ll)<r-1 or len(ll)==0: return False
        if r==1:
            return max ([[s1+s2*((x[1]-cst)/(k**d)),(x[1]-cst)/(k**d)],[[x[3],1]]] 
                        for x in ll)
    
        # Case times k
        res = [[next (s1+k*cst,s2+k**(d+1),k*cst,d+1,k*x[0],k*x[1],
                      [e for e in l if e[2]>x[2]], r-1),
                [x[3],1]] for x in ll if x[1]>=x[0]]
        
        # Case adds k
        res += [[next (s1+cst+k,s2+k**d,cst+k,d,x[0]+k,x[1]+k,
                       [e for e in l if e[2]>x[2]], r-1),
                 [x[3],0]] for x in ll if x[1]>=x[0]]
    
        ll = [e for e in res if e[0]!=False]
        if len(ll)==0: return False
        M = max (ll)
        return [M[0][0], [M[1]]+M[0][1]]
    
    l = next (0,1,0,0,0,10**16,a,n)
    if l==False:
        print("NO")
    else:    
        print("YES")
        c = l[0][1]
        for e in l[1]:
            print e[0], c
            if e[1]: c*=k
            else:    c+=k
    
    
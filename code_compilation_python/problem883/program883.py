def program883():
    ties=int(input())
    scarves=int(input())
    vests=int(input())
    jackets=int(input())
    s1=int(input())
    s2=int(input())
    
    #s1=tie+jacket
    #s2=scarf+vest+jacket
    
    cost1=0
    cost2=0
    
    if s1>=s2:
        k=min(ties,jackets)
        cost1+=(k*s1)
        j2=jackets-k
        l=min(scarves, vests, j2)
        cost1+=(l*s2)
    
    if s1<=s2:
        l=min(scarves, vests, jackets)
        cost2+=(l*s2)
        j1=jackets-l
        k=min(ties,j1)
        cost2+=(k*s1)
        
    if s1>s2:
        print(cost1)
        
    elif s1<s2:
        print(cost2)
        
    elif s1=s2:
        print(max(cost1,cost2))
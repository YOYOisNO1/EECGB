def program3949():
    s1=input()
    s2=input()
    n=len(s1)
    m=len(s2)
    from collections import Counter 
    c1=Counter(s1)
    c2=Counter(s2)
    if c1['2'] and c1['5']:
        have=(c2['2']+c2['5'])//2 
    elif c1['2'] or c1['5']:
        have=c2['2']+c2['5']
    if c1['6'] and c1['9']:
        have2=(c2['6']+c2['9'])//2 
    elif c1['6'] or c1['9']:
        have2=c2['6']+c2['9']
    mini=10**9 
    for i in c1.keys():
        if i not in "2569" and c1[i]:
            mini=min(mini,c2[i]//c1[i]) 
    if c1['2'] or c1['5']:
        mini=min(mini,have)
    if c1['6'] or c1['9']:
        mini=min(mini,have2)
    print(mini if mini!=10**9 else 0 )
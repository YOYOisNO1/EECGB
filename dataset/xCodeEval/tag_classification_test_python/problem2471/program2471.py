def program2471():
    n=input()
    l=(input())
    i=0
    c=0
    lw=0
    done=False
    while i<len(l):
        tl=0
        while i<n and (l[i]!="_" and l[i]!="("):
            i=i+1
            tl=tl+1
        if tl>lw:
            lw=tl
        if i>n-1:
            break
        if l[i]=="(":
            t=i
            while i<n and l[i]!=")":
                i=i+1
            r="".join(l[t+1:i])
            ll=r.split('_')
            j=0
            while j<len(ll):
                if ll[j]=='':
                    del ll[j]
                else:
                    j=j+1
            c=c+len(ll)
        if i>n-1:
            break
        i=i+1
    print(lw,c)
    
    
    
    
    
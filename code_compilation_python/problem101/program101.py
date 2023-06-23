def program101():
    good=[4,7]
    j=0 
    for i in range(1000):
        good.append(good[j]*10+4)
        good.append(good[j]*10+7)
        j+=1 
        
    good.sort() 
    good=[i for i in good if i<=10**20]
    l,r=map(int,input().split())
    if abs(r-l)<=1000:
        ans=0 
        for i in range(l,r+1):
            for j in range(i,i+100000000):
                if j in good:
                    ans+=j 
                    break 
        print(ans)
        exit()
    ans=0 
    lo=0 
    ind1=-1 
    ind2=-1 
    hi=len(good)-1
    nextl=l 
    while lo<=hi: 
        mi=(lo+hi)>>1 
        if good[mi]>=l:
            nextl=good[mi]
            ind1=mi 
            hi=mi-1 
        else:
            lo=mi+1 
    lo=0 
    hi=len(good)-1
    while lo<=hi: 
        mi=(lo+hi)>>1 
        if good[mi]>=r:
            nextr=good[mi]
          #  ind1=mi 
            hi=mi-1 
        else:
            lo=mi+1 
    prevr=r   
    lo=0 
    hi=len(good)-1
    while lo<=hi:
        mi=(lo+hi)>>1 
        if good[mi]<=r: 
            prevr= good[mi]
            ind2=mi 
            lo=mi+1 
        else: 
            hi=mi-1 
    ans=0 
    for i in range(ind1,ind2):
        diff=good[i+1]-good[i] 
        ans+=diff*good[i+1]
    ans+=(nextl-l+1)*nextl 
    ans+=(r-prevr)*nextr   
    print(ans)
def program197():
    p=list(map(int, input().split()))
    n=p[0]
    k=p[1]
    s=input().strip()
    s=list(s)
    s.sort()
    s2=s
    i=0
    sums=ord(s2[0])
    sums=sums-96
    count=1
    while(count<k):
        for j in range(i+1, len(s2)):
            if(abs(ord(s2[j])-ord(s2[i]))>=2 and count<k):
                sums+=ord(s2[j])
                sums=sums-96
                i=j
                count+=1
                break
            else:
                continue
    
    
    if((1<=k<n<=50)==False):
        sums=-1
    if(count<k):
        sums=-1
    if(len(s)!=n):
        sums=-1
        
    print(sums)
    
    
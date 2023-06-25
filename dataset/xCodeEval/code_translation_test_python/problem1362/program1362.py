def program1362():
    n=input()
    l=[int(x) for x in n]
    
    
    
    sum1=0
    k=len(n)
    ans=0
    j=0
    if k==1:
        ans=int(n)
        sum1=ans
    elif k>=2:
        for i in range(k-1,0,-1):
           ans=ans+9*(10**j)
           sum1+=9
           j+=1
        ans+=(int(n[i-1])-1)*(10**j)
        sum1+=int(n[i-1])-1   
        k=str(ans)
        #print(k)
        k=list(k)
        if k[0]=='9':
            k.insert(0,'1')
        else:    
            k[0]=str(int(k[0])+1)
        #print(k)
        while i<len(k)-1:
           if n > ''.join([k[0]]+k[1:i]+['8']+k[i+1:]):
               ans=''.join([k[0]]+k[1:i]+['8']+k[i+1:])
               i=i+1
           else:
               break
    
    #print(k)
    
    s=sum(l)
    if s>=sum1:
        print(''.join(n))
    else:
        print(ans)
    
def program3186():
    '''
    Created on Jan 26, 2012
    
    @author: Moatasem
    '''
    a=list(input())
    curr=a[0]
    cnt=0;
    n=0;
    #print(len(a))
    for i in range(len(a)):
        if(i<len(a)-1 and a[i]==a[i+1]):
            cnt+=1
            if(cnt==5):
                n+=1
                cnt=0
        
        else:
            n+=1
            curr=a[i]
            cnt=0
            
    if(cnt!=0):
        n+=1
    
    print(n)
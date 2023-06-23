def program3013():
    Last login: Sat Jun 20 09:37:04 on console
    bogon:~ yanzhensong$ cd Desktop/
    bogon:Desktop yanzhensong$ vim cf.py 
    
    bogon:Desktop yanzhensong$ vim cf.py 
    bogon:Desktop yanzhensong$ vim cf.py 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    w,m=map(int,input().split());
    bit=[];
    ct=[];
    for i in range(101):
        ct.append(0);
    k=m;
    while(k>0):
        bit.append(k%w);
        k/=w;
    for i in range(len(bit)):
        if(bit[i]==w-1):
            ct[i+1]+=1
            ct[i]-=1
        else:
            ct[i]+=bit[i]
    while(1):
        flag1=0
        flag2=0
        for i in range(101):
            if(ct[i]==0 or ct[i]==1 or ct[i]==-1 ):
                continue
            elif(ct[i]==w-1):
                ct[i]=-1
                ct[i+1]+=1
                flag1=1
            elif(ct[i]==1-w):
                ct[i]=1
                ct[i+1]-=1
                flag1=1
            else:
                flag2=1
        if(flag1==1): continue
        if(flag2==1):
            print 'NO'
            exit()
        break
    print 'YES'
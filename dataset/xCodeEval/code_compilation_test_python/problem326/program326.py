def program326():
    import math
    x=input().split(' ')
    n=int(x[0])
    k=int(x[1])
    
    last=n*(10**k)
    i=1
    cnt=0
    save=-1
    while i<=10000000:
        if (n*i)%10==0:
            zeros=0
            a=n*i
            while a>0:
                b=a%10
                if b==0:
                    zeros=zeros+1
                else:
                    break
                a=a/10
             
            if save!=-1:
                if zeros>savez:
                    save=n*i
                    savez=zeros
            else:
                save=n*i
                savez=zeros
            cnt=1
        i=i+1
    
    if cnt==1:
        i=1
        p=10**k
        while 1:
            if (save*i)%p==0:
                break
            i=i*10
        if (save*i)<last:
            ans= save*i
        else:
            ans= last
    else:
        ans=last
    
    save=-1
    cnt=0
    i=10**k
    while 1:
        j=1
        while j<10:
            if j*i>last:
                cnt=2
                break
            if (j*i)%n==0:
                cnt=1
                save=j*i
                break
            j=j+1
        if cnt==1 or cnt==2:
            break
        i=i*10
    if cnt==1:
        ans=min(ans, save)
    else:
        ans= min(ans,last)
    
    print ans
        
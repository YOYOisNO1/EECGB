def program3993():
    
     from math import log
    n=input()
    b=bin(n)[2:]
    if n==2:
        print 1
    elif n==3:
        print 3
    else:
        n-=1
        b=bin(n)[2:]
        l=len(b)
        ans=0
        for i in range(1,l):
            val=0
            pre=pow(2,i-1)
            if i==1:
                ans+=1
                continue
            for j in range(i-1):
                val+=(pow(2,j)*pre)/2
                pre/=2
            ans+=val
            
        #print ans
        
        if pow(2,int(log(n)/log(2)))==n:
            print ans+ pow(2,int(log(n)/log(2))+1)-2
        else:
            #print b
            for i in range(l-1):
                ans+=pow(2,l-i-1)
            for i in range(1,l):
                if b[i]=='1':
                    val=0
                    pre=pow(2,l-i-1)
                    for j in range(l-i-1):
                        val+=(pow(2,j)*pre)/2
                        pre/=2
                    ans+=val
                    ans+=pow(2,l-i-1)
            print ans
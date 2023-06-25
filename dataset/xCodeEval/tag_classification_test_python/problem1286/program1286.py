def program1286():
    ls=list(map(int, input().split()))
    n=ls[0]
    p=ls[1]
    k=1
    success=False
    if p>0:
        while n-k*p>0:
            x=(str(bin(n-k*p)))[2:]
            count1=0
            for j in x:
                if j=='1':
                    count1+=1
            if count1<=k and k<=n-k*p:
                print(k)
                success=True
                break
            k+=1
        if success==False:
            print(-1)
    elif p==0:
        x=(str(bin(n)))[2:]
        count1=0
        for j in x:
            if j=='1':
                count1+=1
        if count1>0:
            print(count1)
        else:
            print(-1)
            
    elif p<0:
        while success==False:
            while n-k*p<0:
                k+=1
            x=(str(bin(n-k*p)))[2:]
            count1=0
            for j in x:
                if j=='1':
                    count1+=1
            if count1<=k and k<=n-k*p:
                print(k)
                success=True
                break
            k+=1
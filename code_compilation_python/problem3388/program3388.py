def program3388():
    n=input()
    dict={}
    i=n
    arr=[]
    while(i>0):
        k=0
        for j in range(n-i+1):
            arr.append([i,k,k+i])
            k+=1
        i-=1
    
    l=len(arr)
    ans=0
    for i in range(1,l):
        k=arr[i][0]
        l1=arr[i][1]
        l2=arr[i][2]
        if arr[i][0]!=-1:
            found=False
            for j in range(i+1,l):
                if arr[j][0]!=-1:
                    p=arr[j][0]
                    r1=arr[j][1]
                    r2=arr[j][2]
                    if k+p==n and (r1>=l2 or l1>=r2):
                        arr[j][0]=-1
                        ans+=1
                        found=True
                        break
                    elif k+p<n and (r1>=l2 or l1>=r2):
                        p+=arr[j][0]
                        arr[j][0]=-1
            if found!=True:
                ans+=1
    
        #print arr,ans
    
    print ans+1
    
    
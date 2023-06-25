def func(m, count=0):
        l=len(str(m))
        arr=[0]*(l+2)
        arr[1]=1
        for i in xrange(2,l+2):
            arr[i]=arr[i-1]+pow(10,i-1)
        if (arr[l+1]-m>=m-arr[l]):
            t=abs(m-arr[l]) 
            count+=l
        elif arr[l+1]-m<m-arr[l]:
            t=abs(arr[l+1]-m)
            count+=l+1
        #print count, t
        if t==0:
            print count
        if t==1:
            print count+1
        else:
            func(t, count=count)
        
    test=int(input())
    func(test)
def program7730():
    tz=1
    for tcc in xrange(0,tz):
        n,m,d=(int(i) for i in input().split())
        l1=[]
        l2=[]
        c=0
        w=0
        for i in xrange(0,n):
            cw=[int(i) for i in input().split()]
            cw[1]=-cw[1]
            l1.append(cw)
        for i in xrange(0,m):
            cw=[int(i) for i in input().split()]
            cw[1]=-cw[1]
            l2.append(cw)
        l1.sort(reverse=True)
        l2.sort(reverse=True)
        x=0
        y=0
        for i in xrange(0,n):
            l1[i][1]*=-1
        for i in xrange(0,m):
            l2[i][1]*=-1
            x+=l2[i][0]
            y+=l2[i][1]
            l2[i]=[x,y]
        width=0
        ans=0
        mx=0
        #print(l1)
        #print(l2)
        for i in xrange(0,n):
            width+=l1[i][1]
            ans+=l1[i][0]
            rem=d-width
            if(rem<0):
                break
            lo=0
            hi=m-1
            while(hi-lo>1):
                mid=(lo+hi)/2
                if(l2[mid][1]>rem):
                    hi=mid-1
                else:
                    lo=mid
            if(l2[hi][1]<=rem):
                mx=max([mx,ans+l2[hi][0]])
            elif(l2[lo][1]<=rem):
                mx=max([mx,ans+l2[lo][0]])
        print(mx)
        
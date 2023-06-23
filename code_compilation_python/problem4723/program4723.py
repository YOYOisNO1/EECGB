def program4723():
    from collections import defaultdict as dd
    import sys
    input=sys.stdin.readline
    n=int(input())
    l=list(map(int,input().split()))
    if(len(l)>60):
        print(1)
    else:
        xo=[l[0]]
        for i in range(1,n):
            xo.append(l[i]^xo[-1])
        ans=-1
        for gap in range(1,100):
            for i in range(n):
                j=i+gap
                if(j>=n):
                    continue
                if(i>0):
                    val=xo[j]^xo[i-1]
                    if(val<l[i-1]):
                        ans=gap
                        break
                else:
                    val=xo[j]
                if(j+1<n):
                    if(val>l[j+1]):
                        ans=gap
                        break
            if(ans!=-1):
                break
        #print(ans)
        if(ans==-1):
            ans=n
        for i in range(2,n):
            ll=i+2
            #print(n,l)
            for ii in range(n-ll+1):
                j=ii+ll-1
                #print(ii,j,le)
                for m in range(1,ll-2):
                    if(ii>0):
                        le=xo[ii+m]^xo[ii-1]
                    else:
                        le=xo[ii+m]
                    #print(j,ii+m-1,"lol")
                    re=xo[j]^xo[ii+m]
                    #if(i==21):
                    #print(le,re,ii,ii+m,j)
                    if(le>re):
                        ans=min(i,ans)
                        break
                if(ans!=n):
                    break
            if(ans!=n):
                break
        for i in range(n-1):
            cx=l[i]^l[i+1]
            if(i>0):
                if(cx<l[i-1]):
                    ans=1
                    break
            if(i+2<n):
                if(cx>l[i+2]):
                    ans=1
                    break
        if(ans==n):
            print(-1)
        else:
            print(ans)
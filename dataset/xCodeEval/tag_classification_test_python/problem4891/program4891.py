    import sys
    import math
    from collections import defaultdict
    ans=0
def get(dic,cur,size,ans,arr,vis):
        if vis[tuple(arr)]==1:
            return 0
        vis[tuple(arr)]=1
        res=fac[size]
        for i in cur:
            res//=fac[cur[i]]
        #print(res,'ans',size,'size',cur,'cur',dic,'dic')
        if cur['0']>0:
            y=fac[size-1]
            for i in cur:
                if i!='0':
                    y//=fac[cur[i]]
                else:
                    y//=fac[cur[i]-1]
            res-=y
        #print(res,'res')
        ans+=res
        #print(ans,'adnekw')
        res2=0
        for j in dic:
            if dic[j]>=1:
                temp=cur.copy()
                temp[j]+=1
                dictemp=dic.copy()
                dictemp[j]-=1
                arr[int(j)]-=1
                x=get(dictemp,temp,size+1,ans,arr,vis)
                arr[int(j)]+=1
                res2+=x
                #print(x,'x')
                #ans+=x
        return res+res2
    s=sys.stdin.readline()[:-1]
    fac=[1]
    for i in range(1,30):
        x=fac[-1]*i
        fac.append(x)
    #print(fac,'fac')
    dic=defaultdict(int)
    n=len(s)
    arr=[0 for _ in range(10)]
    for i in range(n):
        dic[s[i]]+=1
        arr[int(s[i])]+=1
    cur=defaultdict(int)
    for i in dic:
        dic[i]-=1
        cur[i]+=1
        arr[int(i)]-=1
    #vis[tuple(arr)]=1
    #print(ans,'ansnsnns')
    vis=defaultdict(int)
    x=get(dic,cur,len(dic),ans,arr,vis)
    print(x)
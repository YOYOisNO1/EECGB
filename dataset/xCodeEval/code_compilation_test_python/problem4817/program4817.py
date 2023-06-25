    n=int(input())
    nums=input().split(' ')
    l=[0]*4
    for i in range(4):
        l[i]=int(nums[i])
    t=tuple(l)
    a,b,c,d=t
    p=[0]*(n+1)
    nums=input().split(' ')
    mp=[list() for _ in range(n+1)]
    for i in range(2,n+1):
        p[i]=int(nums[i-2])
        
        mp[p[i]].append(i)
    s=[0]*(n+1)
def sof(i):
        if s[i]!=0:
            return s[i]
        if len(mp[i])>0:
            res=0
            for son in mp[i]:
                res+=sof(son)
            s[i]=res
            return res
        else:
            s[i]=1
            return 1
    rootofl=list()
    for leaf in l:
        while p[leaf]!=1:
            leaf=p[leaf]
        rootofl.append(leaf)
    rootlist=list()
    for rootson in mp[1]:
        if not rootson in rootofl:
            rootlist.append(rootson)
def canpick(a,des):
        if des==0:
            return True
        picklist=rootlist[:]
        for j in range(2):
            cur=a[j]
            while p[cur]!=1:
                fa=p[cur]
                for i in mp[fa]:
                    if i!=cur :
                        picklist.append(i)
                cur=fa
        v=[False]*(n+1)
        v[0]=True
        for i in range(len(picklist)):
            val=sof(picklist[i])
            if des-val>=0 and v[des-val]:
                return True
            for j in range(des-val,-1,-1):
                if  v[j] :
                    v[j+val]=True
        return False
    
    m=sof(1)
    if m%2==1:
        print('NO')
    else:
        v1=m//2-1-sof(rootofl[2])
        v2=m//2-1-sof(rootofl[0])
        if canpick([a,b], v1) and canpick([c,d], v2):
            print('YES')
        else:
            print('NO')
    
    
    
    
        
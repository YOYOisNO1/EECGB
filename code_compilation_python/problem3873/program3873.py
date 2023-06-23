    a,b=map(int,input().split())
    c,d=map(int,input().split())
    v1=a*b
    v2=c*d
    from collections import defaultdict
    s=defaultdict(int)
    s[v1]=0
def dfs(v1,c):
       # print v1
        if v1==1:
            return 0
        if v1%3==0:
            if 2*v1/3 in s:
                s[2*v1/3]=min(s[2*v1/3],c+1)
            else:
                s[2 * v1 / 3]=c+1
    
            dfs(2*v1/3,c+1)
        if v1%2==0:
            if v1/2 in s:
                s[v1/2]=min(s[v1/2],c+1)
            else:
                s[v1/2]=c+1
            dfs(v1/2,c+1)
    
    dfs(v1,0)
    from copy import deepcopy
    f2=deepcopy(s)
    s=defaultdict(int)
    s[v2]=0
    dfs(v2,0)
    f1=deepcopy(s)
    ans=1892
    temp=[]
    #print f1,f2
    for i in f1:
        if i in f2:
    
            ans=min(ans,(f1[i]+f2[i]))
            temp.append((f2[i],f1[i],i))
def helper(cv,a,b,op):
        for i in range(0,30):
            for j in range(0,30):
                for k in range(0,30):
                    for l in range(0,30):
                        ok1=0
                        ok2=0
                        ta=0
                        tb=0
                        if i+j+k+l==op:
                            if i>j:
                                ta=a*pow(2,i-j)
                                if ta%(pow(3,i))==0:
                                    ok1=1
                                    ta=ta/pow(3,i)
                            elif a%((pow(3,i)*pow(2,j-i)))==0:
                                ok1=1
                                ta=a/((pow(3,i)*pow(2,j-i)))
                            if k>l:
                                tb=b*pow(2,k-l)
                                if tb%(pow(3,k))==0:
                                    tb=tb/pow(3,k)
                                    ok2=1
                            elif b%((pow(3,k)*pow(2,l-k)))==0:
                                tb=b/((pow(3,k)*pow(2,l-k)))
                                ok2=1
                        #print ok1,ok2,ta,tb
                        if ok1 and ok2 and ta*tb==cv:
                            return ta,tb
    
    
    
    
    
    
    if ans==1892:
        print -1
    else:
        temp.sort()
       # print temp
        op1=temp[0][0]
    
        op2=temp[0][1]
        val1=temp[0][2]
       # print val1,op1,a,b,op2
        n1,n2=helper(val1,a,b,op1)
        n3, n4 = helper(val1, c, d, op2)
    
        print ans
        print n1,n2
        print n3,n4
    
    
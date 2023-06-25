    # code
    ''' LIS
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a1 = [1 for _ in range(n)]
        i, j = 1, 0
        while (i < n ):
            #print(i,j,a[i],a[j])
            if a[i] > a[j]:
                #print(a1[i],a1[j])
                a1[i] =max(1+ a1[j],a1[i])
                j += 1
            else:
                j += 1
            if i == j:
                j = 0
                i += 1
     
        print(a1)
    #LCSubstring
    t=int(input())
    for _ in range(t):
        a,b=map(int,input().split())
        s1=input()
        s2=input()
        n=[[0 for _ in range(b+1)]for _ in range(a+1)]
        r=0
        for i in range(1,a+1):
            for j in range(1,b+1):
                print(i,j)
                if i==0 or j==0:
                    n[i][j]=0
                    continue
                elif s1[i-1]==s2[j-1]:
                    print("here",n[i-1][j-1])
                    n[i][j]=1+n[i-1][j-1]
                    r=max(r,1+n[i-1][j-1])
                    print(n)
        print(r)
    #LCSubsequnce
    t=int(input())
    for _ in range(t):
        a,b=map(int,input().split())
        s1=input()
        s2=input()
        n=[[0 for _ in range(b+1)]for _ in range(a+1)]
        r=0
        for i in range(1,a+1):
            for j in range(1,b+1):
                if i==0 or j==0:
                    n[i][j]=0
                    continue
                elif s1[i-1]==s2[j-1]:
     
                    n[i][j]=1+n[i-1][j-1]
                else:
                    n[i][j]=max(n[i-1][j],n[i][j-1])
        print(n[a][b])
     
    #Hopping stones
def score(m,trip_jump,step):
     
        if m==n-1:
            return step*a[m-1]
        if m==n-2:
            return step*a[m]+a[m+1]
        if m==n-3:
            return max(a[m]+a[m+1],2*a[m+1])
        else:
            if trip_jump==1:
                return step*a[m]+max(score(m+1,1,1),score(m+2,1,2))
            else:
                 return step*a[m]+max(score(m+3,1,3),score(m+2,0,2),score(m+1,0,1))
     
     
    n=int(input())
    a=list(map(int,input().split()))
    print(score(0,0,1),score(1,0,2),score(2,1,3))
     
    #Uncertain steps
def count(n,trip_step):
        if n==0:
            return 1
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            if trip_step==0:
                return 4
            else:
                return 3
        if trip_step==0:
            return count(n-1,0)+count(n-2,0)+count(n-3,1)
        else:
            return count(n-1,0)+count(n-2,0)
     
    n=int(input())
    print(count(n,0))
    #GRID atcoder
    import sys
    sys.setrecursionlimit(20000)
     
def paths(i, j):
     
        if i == h - 1 and j == w - 1:
            return 1
        if a[i][0][j] == '#':
            return 0
        if i < h - 1 and j < w - 1:
            if dp[i][j] == -1:
                dp[i][j] = paths(i + 1, j) + paths(i, j + 1)
                return dp[i][j]
            else:
                return dp[i][j]
        elif i == h - 1 and j < w - 1:
            if dp[i][j] == -1:
                dp[i][j] = paths(i, j + 1)
                return dp[i][j]
            else:
                return dp[i][j]
        elif i < h - 1 and j == w - 1:
            if dp[i][j] == -1:
                dp[i][j] = paths(i + 1, j)
                return dp[i][j]
            else:
                return dp[i][j]
     
     
    h, w = map(int, input().split())
    a = [[] for _ in range(h)]
    m = 1000000007
    for i in range(h):
        a[i].append(input())
    dp = [[-1 for _ in range(1000)] for _ in range(1000)]
    print(paths(0, 0) % m)
     
    #Coins atCoder
    import sys
     
    sys.setrecursionlimit(20000)
     
     
def getCombi(h, t, n, s):
     
        global subsum
        global tp
        print("called for", h, t, n, s, subsum)
        if len(s) == n:
            tp+=subsum
            combs.append(s)
            print('compl',subsum,tp)
            subsum=1
            return
        if h > 0:
            subsum *= p[len(s) ]
            print('in h',subsum,s)
            getCombi(h - 1, t, n, s + 'h')
     
        if t > 0:
            subsum *= (1 - p[len(s)])
            print('in t',subsum,s)
            getCombi(h, t - 1, n, s + 't')
     
     
    n = int(input())
    p = list(map(float, input().split()))
    dp=[[0 for _ in range(n+1)]for _ in range(n+1)]
    dp[0][0]=1 #j no. of heads in i coins
    for i in range(1,n+1):
        for j in range(i+1):
            if j==0:
                dp[i][j]=dp[i-1][j]*(1-p[i-1])
            else:
                dp[i][j] = dp[i - 1][j] * (1 - p[i-1]) + dp[i-1][j-1]*p[i-1]
    print(dp)
     
    #maximize sum Maximize the sum of selected numbers from an array to make it empty
def getMax(a,n,sel,ind,ans):
        print("im function",a,n,sel,ind,ans)
        if len(a)==1:
            ans=max(ans,ans+a[0])
            print(ans,"abs")
            bs.append(ans)
            return
        selected=sel
        selp1=sel+1
        selm1=sel-1
        f=0
        l2=[]
        f1=-1
        f2=-1
        f0=-1
        print("updating list")
        for k in range(n):
            if a[k]!=selected and a[k]!=selm1 and a[k]!=selp1:
                l2.append(a[k])
            elif a[k]==selected:
                if f0==-1:
                   ans+=a[k]
                   f0=0
                   continue
                else:
                    l2.append(a[k])
            else:
                if a[k]==selp1:
                    if f1==-1:
                       f+=1
                       f1=0
                       continue
                    else:
                        l2.append(a[k])
                if a[k]==selm1:
                    if f2==-1:
                        f+=1
                        f2=0
                        continue
                    else:
                        l2.append(a[k])
        print("updated",l2,ans)
        if len(l2)==0:
     
            bs.append(ans)
            ans = 0
            return
        for t in range(len(l2)):
             getMax(l2,n-1-f,l2[t],t,ans)
     
    a=list(map(int,input().split()))
    n=len(a)
    ans=0
    bs=[]
    for i in range(n):
        getMax(a,n,a[i],i,ans)
    print(max(bs))
    '''
    #maximum sum optimised
    '''
     
    #01 knapsack
def knap(n,cap):
        if n==0 or cap==0:
            return 0
        if weight[n-1]>cap:
            return knap(n-1,cap)
        else:
            return max(knap(n-1,cap),values[n-1]+knap(n-1,cap-weight[n-1]))
     
    n=int(input())
    cap = int(input())
    values = list(map(int,input().split()))
    weight = list(map(int,input().split()))
    print(knap(n,cap))
    dp=[[0 for _ in range(n+1)]for _ in range(cap+1)]
    for i in range(cap+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif weight[j-1]>i:
                dp[i][j]= dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],weight[j-1]+dp[i-1][j-weight[j-1]])
    print(dp[n][cap])
     
def count(r,c,k):
        if c==n-1 and k>0:
            return 0
        if c>n-1:
            return 0
        if k==0:
            return 1
        if dp[k][r][c]==-1:
            a=0
            if r==0:
                a+=count(1,c+1,k-1)
            else:
                a+=count(0,c+1,k-1)
            for l in range(c+2,n):
                a+=count(1,l,k-1)
                a+=count(0,l,k-1)
            dp[k][r][c]=a
        return dp[k][r][c]
     
    t=int(input())
    for _ in range(t):
        dp = [[[-1 for _ in range(1001)] for _ in range(2)]for _ in range(1001)]
        n,k=map(int,input().split())
        ans=0
        if k>n:
            print(ans)
            continue
        for i in range(n):
            ans+=count(0,i,k-1)+count(1,i,k-1)
        print(ans%1000000007)
    ######
    DP Matrix chain multiplication
    
def brcc(i, j, n):
    
        global nn
        if i== j:
            print(nn, end='')
            nn = chr(ord(nn) + 1)
            return
        print('(', end='')
        brcc(i, brc[i][j], n)
        brcc(brc[i][j] + 1, j, n)
        print(')', end='')
    
    
def getmin(i, j):
        if j <= i+1:
            return 0
        if dp[i][j] == -1:
            c = float('inf')
    
            for k in range(i + 1, j):
                c1 = getmin(i, k) + getmin(k, j) + a[i] * a[k] * a[j]
                if c1 < c:
                    c = c1
                    dp[i][j]=c
                    brc[i+1][j] = k
        return dp[i][j]
    
    print(list(zip([i + 1 for i in range(5)], [] * 5)))
    g = dict.fromkeys(list(zip([i + 1 for i in range(5)], [] * 5)))
    print(g)
    t = int(input())
    for _ in range(t):
        n = int(input())
        nn='A'
        a = list(map(int, input().split()))
        dp = [[-1 for _ in range(n )] for _ in range(n )]
        for k in range(n):
            dp[k][k]=0
        brc = [[0 for _ in range(n)] for _ in range(n)]
        getmin(0, n - 1)
        print(dp[0][n-1])
        brcc(1, n-1, n)
    '''
def count(k1,k2,kf,kh):
        global k11
        global k22
    
        if kf>k11 or kh>k22:
            return 0
        if k1==0 and k2==0:
            return 1
    
    
        if dp[k1][k2][kf][kh] == -1:
         if k2>0 and k1==0:
            dp[k1][k2][kf][kh] =count(k1,k2-1,0,kh+1)
         if k1>0 and k2==0:
             dp[k1][k2][kf][kh] =count(k1-1,k2,kf+1,0)
         if k1>0 and k2>0:
             dp[k1][k2][kf][kh] =count(k1-1,k2,kf+1,0)+count(k1,k2-1,0,kh+1)
        return dp[k1][k2][kf][kh]
    n1,n2,k11,k22=map(int,input().split())
    dp=[[[[-1 for _ in range(k22+1)]for _ in range(k11+1)]for _ in range(n2+1)]for _ in range(n1+1) ]
    ans=count(n1,n2,0,0)
    print(ans%100000000)
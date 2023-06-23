    '''#problem1
    n=int(input())
    price=[int(i) for i in input().split()]
    q=int(input())
    acc=[]
    for i in range(q):
        k=int(input())
        acc.append(k)
    price.sort()
def search(k,arr):
        l=0
        r=len(arr)-1
        ans=0
        while l<=r:
            mid=l+int((r-l)/2)
            if arr[mid]<=k:
                ans=mid+1
                l=mid+1
            else:
                r=mid-1
        return ans
    for j in acc:
        a=search(j,price)
        print(a)'''
    
    
    '''n=int(input())
    nums=[int(i) for i in input().split()]
    s=sum(nums)
    ans=0
    if s%3!=0:
        ans=0
        
    else:
        s/=3
        cnt=[0]*(n)
        sum=0
        for i in range(n-1,-1,-1):
            sum+=nums[i]
            if sum==s:
                cnt[i]=1
        for j in range(n-2,-1,-1):
            cnt[j]+=cnt[j+1]
        sum=0
        k=0
        while k+2<n:
            sum+=nums[k]
            if sum==s:
                ans+=cnt[k+2]
                
            k+=1
    print(ans)'''
    
    
    n,k,d=[int(i) for i in input().split()]
    ans=0
    dp=[[0,0] for j in range(n+1)]
    dp[0][0]=1 
    dp[0][1]=0
    for i in range(1,n+1):4 5 2
        for j in range(1,k+1):
            if i-j<0:
                break
            if j<d:
                dp[i][0]+=dp[i-j][0]
                dp[i][1]+=dp[i-j][1]
            else:
                dp[i][1]+=dp[i-j][0]
                dp[i][1]+=dp[i-j][1]
    print(dp[n][1]%(10**9+7))
    
    from itertools import permutations
    r,b,g=list(map(int,input().split()))
    lis=permutations([0,1,2,3])
def function(num,arr):
        ans=0
        for i in range(4):
            if num[i]==0:
                if arr[0]>2:
                    temp=arr[0]//3
                    arr[0]-=(3*temp)
                    ans+=temp
            elif num[i]==1:
                if arr[1]>2:
                    temp=arr[1]//3
                    arr[1]-=(3*temp)
                    ans+=temp
            elif num[i]==2:
                if arr[2]>2:
                    temp=arr[2]//3
                    arr[2]-=(3*temp)
                    ans+=temp
            else:
                if min(arr)>0:
                    temp=min(arr)
                    arr[0]-=temp
                    arr[1]-=temp
                    arr[2]-=temp
                    ans+=temp
        return ans
    ans=0
    for i in lis:
        arr=[r,b,g]
        ans=max(ans,function(i,arr))
    print(ans)
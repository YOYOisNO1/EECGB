    N = int(input())
    nums = list(map(int,input().split()))
    for i in range(N):
        nums[i] -= 1
    arr = [1]
    f = 0
    for i in range(N):
        checked = [0 for x in range(N)]
        cnt = 1
        cur = nums[i]
        while cur != i:
            if checked[cur]:
                f = 1
                break
            checked[cur] = 1
            cur = nums[cur]
            cnt += 1
        if cnt%2==0:
            arr.append(cnt/2)
        else:
            arr.append(cnt)
    
def gcd(a,b):
        if not b:
            return a
        return gcd(b,a%b)
    
    ans = arr[0]
    for i in range(1,len(arr)):
        cur = gcd(ans,arr[i])
        ans = (ans*arr[i])/cur
    if f:
        print(-1)
    else:
        print(ans)
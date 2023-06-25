def cal(x):
        ans=0
        while x:
            ans+=x%10
            x=x//10
        return ans
    k=int(input())
    n=10
    while k:
        n+=9
        if cal(n)==10:
            k-=1
    print(n)
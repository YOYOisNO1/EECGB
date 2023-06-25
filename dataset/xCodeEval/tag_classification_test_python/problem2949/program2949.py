    n = int(input())
    f = 18
    ans = 0
def calc(x):
        ans  = 0
        while(x):
            ans+=x%10
            x//=10
        return ans
    while(n):
        f+=1
        if(calc(f)==10):
            n-=1
    print(f)
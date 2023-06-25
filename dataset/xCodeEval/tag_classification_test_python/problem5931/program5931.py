    from sys import stdin
    import math
    n = int(stdin.readline())
    a =  map(int,stdin.readline().split())
    
    ans = -1
    b = set(a)
    a = [0] + a
def gcd(x,y):
        while x%y:
            t = x%y
            x = y
            y = t
        return y
def lcm(x,y):
        return (x*y)/gcd(x,y)
    if len(b)==n:
        di = {}
        ans = 1
        vis = [0]*(n+1)
        for i in a:
            if vis[i]==0:
                vis[i] = 1
                cur = set()
                cur.add(i)
                while True:
                    i = a[i]
                    if vis[i]==1:
                        break
                    vis[i] = 1
                    cur.add(i)
                x = len(cur)                
                if len(cur)%2==0:
                    x = len(cur)/2
                ans = lcm(ans,x)
    print(ans) 
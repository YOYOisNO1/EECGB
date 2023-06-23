def profit(n,d,a,m):
        s = sum(a)
        if m <= n:
            return s
        else:
            return (s-(m-n)*d)
    
    n,d = map(int,input().split())
    a = map(int,input().split())
    m = int(input())
    print profit(n,d,a,m)
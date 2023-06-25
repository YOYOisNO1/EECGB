def program940():
    s=map(int,input().split())
    n=s[0]
    m=s[1]
    rest=n+n/m
    pre=n+n/m
    while n+rest/m!=pre:
        rest=n+rest/m
        pre=rest
    print(rest)
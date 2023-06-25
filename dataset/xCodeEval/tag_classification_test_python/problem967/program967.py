def program967():
    from math import *
    t=1
    while t:
        t=t-1
        n=int(input())
        ra,sa,pa=map(int,input().split())
        rb,sb,pb=map(int,input().split())
        mx=min(ra,sb)+min(sa,pb)+min(pa,rb)
        mn=max(0,ra-rb-pb)+max(0,sa-sb-rb)+max(0,pa-pb-sb)
        print(mn,mx)
        
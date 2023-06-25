def program3164():
    n, R, r = map(int,raw.input().split())
    ans = true
    if (r > R): ans=false
    if (n==1): ans=(r<=R)
    ans = ans&&((R-r)/sin(pi/n)>=r)
    if (ans==false): print("NO")
    else: print("YES")
    from math import *
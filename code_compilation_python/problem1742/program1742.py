def program1742():
    from math import *
    n, m, k = map(int,input().split(' '))
    ans = (2**((n-1)*(m-1)%1000000006))%(1000000007)
    if (k==-1 && (n+m)%2==1) ans=0;
    print(ans)
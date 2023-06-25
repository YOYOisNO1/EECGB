def program6200():
    r,c,r1,c1 = map(int,input().split())
    rk = 1 if r==r1 or c==c1 else 2
    b = 0 if (r+c)%2 != (r1+c1)%2 else (1 if abs(r-r1)==abs(c-c1) else 2)
    k = max(abs(r1-r),abs(c1-c))
    print(rk,b,k)
def check(x):
        if x== False:
            return 0
        else:
            return 1
    
    x, y, z = map(int, input().split())
    x1, y1, z1 = map(int, input().split())
    a = list(map(int, input().split()))
    ans = a[0]*check(y<0) + a[1]*check(y>y1) + a[2]*check(z<0) + a[3]*check(z>z1) + a[4]*check(x<0) + a[5]*check(x>x1)
    print(ans)
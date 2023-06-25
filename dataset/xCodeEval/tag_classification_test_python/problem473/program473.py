    n = input()
    
    vals = map(int, input().split())
    
    c1 = 1
    c2 = 1
    
    for val in vals:
        if val == 100:
            c1 += 1
        else:
            c2 += 1
    
def can_sum(a,b,c,d):
        return any(p1+2*p3==p2+2*p4 for p1,p2 in [(a,c), (c,a)] for p3,p4 in [(b,d), (d,b)])
    
        return a+2*b==c+2*d or a+2*d==c+2*b or c+2*d==a+2*b or c+2*b==a+2*d
    0,1,2,3 ; 0,3,2,1 ; 2,3,0,1 ; 2,1,0,3
    
    for i in range(c1):
        xt1 = c1-i-1
        xo1 = i
        for j in range(c2):
            xt2 = c2-j-1
            xo2 = j
            if can_sum(xt1, xt2, xo1, xo2):
                print("YES")
                exit(0)
    
    print("NO")
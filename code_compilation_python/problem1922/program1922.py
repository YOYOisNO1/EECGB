def program1922():
    
    n,m,x,y,a,b = map(int,input().split())
    
    ans = -1
    for c in [(1,m),(n,1),(n,m),(1,1)]:
        dx = abs(x - c[0])
        dy = abs(y - c[1])
        if dx==0 and dy==0:
            print 0
            exit(0)
        elif dx%a==0 and dy%b==0 and (dx/a)%2==(dy/b)%2:
            if ans==-1:
                ans = max(dx/a,dy/b)
            else:
                ans = min(ans,max(dx/a,dy/b))
    
    if (n-x<a and stx-1<a) or (m-sty<b and sty-1<b):
        ans = -1
    if ans!=-1:
        print ans
    else print "Poor Inna and pony!"
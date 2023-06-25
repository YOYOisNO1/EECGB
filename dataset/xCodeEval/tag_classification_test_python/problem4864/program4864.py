def program4864():
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    
    c1=[sum([a[2*i] for i in range(4)]), sum([a[2*i+1] for i in range(4)])]
    c2=[sum([b[2*i] for i in range(4)]), sum([b[2*i+1] for i in range(4)])]
    
    s=2*max(abs(a[0]-a[2]), abs(a[1]-a[3]))
    d=2*max(abs(b[0]-b[4]), abs(b[1]-b[5]))
    dx=abs(c1[0]-c2[0])
    dy=abs(c1[1]-c2[1])
    
    if dx+dy<=(2*s+d) and dx<=s+d and dy<=s+d:
        print("YES")
    else:
        print("NO")
        
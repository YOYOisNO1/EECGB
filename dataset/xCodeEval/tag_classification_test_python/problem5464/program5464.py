def program5464():
    vals=[int(x) for x in input().split(' ')]
    n=vals[0]
    m=vals[1]
    k=vals[2]
    x=vals[3]
    y=vals[4]
    
    asked=[[0 for i in xrange(0,m)] for j in xrange(0,n)]
    
    do_increment=True
    increment = 1
    if n == 1:
        do_increment = False
        increment = 0
    
    row = 0
    student = 0
    count = 0
    if (n==1): fullcycle = k/m
    else: fullcycle=k/(m*(2*n-2))
    for j in xrange(0,n):
        for i in xrange(0,m):
            if j==0 or j==n-1: asked[j][i]=fullcycle
            else: asked[j][i]=fullcycle*2
    if (n==1): count = fullcycle * m
    else: count=fullcycle*(m*(2*n-2))
    while(count<k):
        asked[row][student]+=1
        student+=1
        if (student >= m):
            if row == n-1 and do_increment: increment = -1
            if row == 0 and do_increment: increment = 1
            row+=increment
            student = 0
        count+=1
    
    flat = [val for row in asked for val in row]
    maxi=max(flat)
    mini=min(flat)
    sergei=asked[x-1][y-1]
    print(str(maxi) + ' ' + str(mini) + ' ' + str(sergei))
        
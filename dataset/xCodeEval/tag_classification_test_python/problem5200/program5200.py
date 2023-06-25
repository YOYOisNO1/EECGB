def program5200():
    from sys import stdin, stdout
    
    n, l, r = map(int, stdin.readline().rstrip().split())
    
    if n>=2:
        i=0
        while 2**i<=n:
            i+=1
        totalNodes=2**i-1
    
    
        minBound=1
        maxBound=2**i-1
        nodeScore=n
        finished=False
        leftScore=0
    
        while not finished:
            if l<(minBound+maxBound)/2:
                maxBound = (minBound+maxBound)/2-1
                nodeScore=nodeScore/2
            elif l==(minBound+maxBound)/2:
                leftScore+=nodeScore/2
                finished=True
            else:
                minBound = (minBound+maxBound)/2+1
                leftScore+=nodeScore/2 + nodeScore%2
                nodeScore=nodeScore/2
            if nodeScore==1:
                finished=True
    
        minBound=1
        maxBound=2**i-1
        nodeScore=n
        finished=False
        rightScore=0
    
        while not finished:
            if r<(minBound+maxBound)/2:
                maxBound = (minBound+maxBound)/2-1
                nodeScore=nodeScore/2
            elif r==(minBound+maxBound)/2:
                rightScore+=nodeScore/2 + nodeScore%2
                finished=True
            else:
                minBound = (minBound+maxBound)/2+1
                rightScore+=nodeScore/2 + nodeScore%2
                nodeScore=nodeScore/2
            if nodeScore==1:
                rightScore+=1
                finished=True
    
        print(rightScore-leftScore)
    elif n==0:
        print(0)
    elif n==1 and l==1:
        print(1)
    else:
        print(0)
        
        
            
def program1075():
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    
    
    maxWin=min(a[0],b[1])+min(a[1],b[2])+min(a[2],b[0])
    
    #bTotalSubtracted=0
    a1=max(0,a[0]-(b[0]+b[2]))
    #bTotalSubtracted+=min(a[0],b[0]+b[2])
    a2=max(0,a[1]-(b[1]+b[0]))
    #bTotalSubtracted+=min(a[1],b[1]+b[0])
    a3=max(0,a[2]-(b[2]+b[1]))
    #bTotalSubtracted+=min(a[2],b[2]+b[1])
    minWin=(a1+a2+a3)
    print('{} {}'.format(minWin,maxWin))
    
    import sys
    import Queue
    import bisect
    import fractions
    import heapq
    
    
    n,k =  map(int ,input().split())
    ans = 0
    
    
    LL = [[0]*(n+1) for i in range(n+1)]
    LL[0][0]=1
    LL = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]
    
    myLL =[[0]*(i+1) for i in range(100)]
    
    
def f(i,j,val):
    
        if myLL[i][j]+val>=1:
            rest = myLL[i][j]+val-1
            myLL[i][j]=1
            f(i+1,j,rest/2)
            f(i+1,j+1,rest/2)
    
        else:
            myLL[i][j] += val
    for t in range(k):
        f(0,0,1.0)
    ans =0
    for i in myLL:
        for j in i:
            if j == 1:
    
                ans+=1
    
    print ans
    
    
    
    
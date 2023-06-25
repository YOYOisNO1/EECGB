def program966():
    N = int(input())
    
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    maxWin = min(a[0],b[1]) + min(a[1],b[2]) + min(a[2],b[0])
    
    maxNotWin = min(a[0],b[0]+b[2]) + min(a[1],b[1]+b[0]) + min(a[2],b[2]+b[1])
    
    
    minWin = 0
    
    if maxNotWin < N:
        minWin = N - maxNotWin
    
    
    print(str(minWin)+" "+str(maxWin))
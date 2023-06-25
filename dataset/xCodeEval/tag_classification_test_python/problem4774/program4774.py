def program4774():
    '''Piles With Stones Solution
    '''
    
    N = int(input())
    
    xlist = list(map(int, input().split()))
    ylist = list(map(int, input().split()))
    
    removed = sum(xlist) - sum(ylist)
    if removed < 0:
        print('No')
    else:
        print('Yes')
    
def program5455():
    n = int(input())
    x,y = list(map(int,input().split()))
    
    black = (n-y)+(n-x)
    white = (y-1)+(x-1)
    
    if white<=black:
    	print('White')
    else:
    	print('Black')
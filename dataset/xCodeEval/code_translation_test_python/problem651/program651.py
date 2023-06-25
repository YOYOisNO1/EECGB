def program651():
    r1, c1, r2, c2 = map(int, input().split(' '))
    
    #rook
    
    if(r1 == r2 or c1==c2):
    	print(1, end=' ')
    else:
    	print(2, end=' ')
    
    
    #bisohop
    if(abs(r1-r2)==abs(c1-c2)):
    	print(1, end=' ')
    elif((abs(r1-r2)%2==0 and abs(c1-c2)%2==0) or (abs(r1-r2)%2!=0 and abs(c1-c2)%2!=0)):
    	print(2, end=' ')
    else:
    	print(0, end=' ')
    
    
    #king
    
    print(max(abs(r1-r2), abs(c1-c2)))
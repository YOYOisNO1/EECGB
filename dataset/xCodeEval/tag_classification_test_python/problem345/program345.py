def program345():
    # -*- coding: utf-8 -*-
    """
    Created on Thu Sep  1 11:10:33 2022
    
    @author: Administrator
    """
    
    
    #for _ in range(int(input())):
    n=int(input())
    
    if n<=5:
        print([3,5,7,8,9][n-1])
    else:    
        a,b=(n-6)//15,(n-6)%15        
        
        print((2*a+1+(b>6))*10+[1,2,3,5,6,7,9,0,1,3,4,5,7,8,9][b])
            
        
        
        
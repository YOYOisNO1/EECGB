    # -*- coding: utf-8 -*-
    """
    Created on Wed Mar  7 09:39:50 2018
    
    @author: wangjun
    """
    import math
    
    
def Grasshopper(ng,nb):
        
        if nb%2 ==0 :
            nb=nb-1
        if nb <= ng:
            return -1
        if ng ==2 :
            return nb
        nng = math.floor( nb ** 0.5 )
        if nng >ng :
            nng=ng
        
        for branch in range(nb,ng,-2):
            flag =True
            for hopper in range(3,nng+1,2):
                if branch % hopper == 0:
                    flag = False
                    break
            if flag==True : 
                if branch > ng :
                    return branch
                else:
                    return -1
        return -1
            
def hello():
        """Print "Hello World" and return None"""
        ar = list(map(int, input().strip().split(' ')))
        
        result=Grasshopper(ar[0],ar[1])
        print(result)
    # main program starts here
    hello()
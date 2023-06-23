def program287():
    # -*- coding: utf-8 -*-
    """
    Created on Fri Dec 30 23:29:21 2016
    
    @author: RandomNone
    """
    n=int(input())
    pos=0
    flag=1
    for i in range(n):
        a=input().split()
        distance=int(a[0])
        direction=a[1]
        if(pos==0 and direction!='South'):
            print 'NO'
            flag=0
            break
            
        elif(pos==20000 and direction!='North'):
            print 'NO'
            flag=0
            break
            
        if(direction=='South'):
            pos+=distance
        if(direction=='North'):
            if(pos>=distance):
                pos-=distance
            else:
                pos+=40000-distance
        pos=pos%40000
    
    if(flag==1):  
        if(pos%40000==0):
            print 'YES'
        else:
            print 'NO'
    
    
        
        
        
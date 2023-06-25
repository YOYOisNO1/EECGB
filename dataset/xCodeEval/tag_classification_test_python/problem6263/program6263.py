    '''
    Created on May 4, 2012
    
    @author: moatasem
    '''
    
def getModIIII(a,b,n):
        if(b==1 ):
            return a%n
        elif (b==0 ):
            return 1
        elif(b%2<>0 ):
            return a*((getModIIII(a,b/2,n))**2)%n
    
        else:
            return ((getModIIII(a,b/2,n))**2)%n
        
    n=int(input())
    if(n==0):
       print(1)
    elif(n==1):
       print(3)    
    else:
       f=  getModIIII(2,n,1000000007)
       print(((f*(f+1))/2) )%1000000007
       
       
        
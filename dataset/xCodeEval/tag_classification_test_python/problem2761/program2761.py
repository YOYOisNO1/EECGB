    '''
    Created on 20 Mar 2011
    
    @author: user
    '''
def valid( G,B):
     if G>B:
        if G-B>1:
            return False
        else:
            return True
     elif G==B:
        return True  
     else:
        
        if B<=2*(G+1) and B>=(G+1):
            return True
        else:
            return False
             
    
    
    
    
    
    n= input().split()
    m=input().split()
    if valid(int(n[0]),int(m[1]))==True or valid(int(n[1]),int(m[0]))==True:
        print("YES")
    else:
        print("NO")
    
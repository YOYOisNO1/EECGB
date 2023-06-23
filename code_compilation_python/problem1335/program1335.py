    #This code is dedicated to Olya S.
    
def e(x):
        s=0
        while x>0:
            s+=x%10
            x//=10
        return s
    
def down(x):
        l=len(x)-1
        if x[0]=='1':
            return '9'*l
        else:
            return str(int(x[0])-1)+'9'*l
        
    n=input()
    if e(int(n))>=e(int(down(n))):
        print(n)
    else:
        print(down(n))
    
            
         
    
    
    
            
    
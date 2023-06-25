    
def bin( temp):
        
        while temp > 1: 
            last = (temp) % 10  
            temp = temp / 10
            if(last !=0):
                g=1
            k++
        m=int(k/2)
        if(g != 1 && k%2==0):
            m=m-1
        return m;
        
    a=input()
    b=bin(a)+1
    print(b)
    
            
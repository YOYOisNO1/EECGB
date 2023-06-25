    citire=list(map(int,input().split()))
    
    k=0
    
def get_p2(n):
        i=1
        while n>=i:
            i*=2
        i-=1
        return int(i)
    
    p=get_p2(citire[0])
    
    suma=0
    
def rez(l,r,len,n):
        global suma
        #print(l,r,len,n)
        jumlen=len//2+1
        len=(len+1)//2-1
        if l<jumlen:
            rez(l,min(jumlen-1,r),len,n//2)
        if l<=jumlen and r>=jumlen:
            suma+=n%2
        if r>jumlen:
            rez(max(1,l-jumlen),r-jumlen,len,n//2)
    
    
    rez(citire[1],citire[2],p,citire[0])
    
    print(suma)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
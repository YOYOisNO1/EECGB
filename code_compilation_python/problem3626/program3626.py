    citire=list(map(int,input().split()))
    
    k=0
    
def get_p2(n):
        i=1
        while n>=i:
            i*=2
        i-=1
        return int(i)
    
    p=get_p2(citire[0])
    
def get_num(i,n,len):
        key=len//2+1
        if i==key:
            return n%2
        elif i>key:
            i-=key
        n//=2
        len=(len+1)//2-1
        return get_num(i,n,len)
    
    for i in range(citire[1],citire[2]+1):
        n=citire[0]
        len=p
        k+=get_num(i,n,len)
    
    print(k)
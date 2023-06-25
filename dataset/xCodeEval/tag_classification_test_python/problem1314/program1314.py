    
    k=input()
    l=input()
    
    
def  mu(x,n):
        kq=1
        for i in range(n):
            kq*=x
        return kq
    
    count=0
    kq=1
    while kq<l and k!=0:
        kq=kq*k
        count+=1
    
    if mu(k,count)==l: 
        print("YES")
        print(count-1)
    else: 
        print("NO")
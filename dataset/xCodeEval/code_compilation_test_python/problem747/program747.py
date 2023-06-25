    n = int(input()) 
    k = int(input()) 
    a = int(input()) 
    b = int(input()) 
def shut(t) :
        if k == 1 :
            return (t-1)*a
        if t < k : 
            return (t-1)*a
        else  : 
            r = t%k 
            return (r*a) +  min(b , a*(t-t//k) + shut(t//k)  
    print(shut(n))
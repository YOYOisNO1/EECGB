    a,b=list(map(int,input().split()))
def compute_gcd(x, y):
       while(y):
           x, y = y, x % y
       return x
    
    k = (a*b)//compute_gcd(a,b)
    D=(k/a)-1
    M=(k/b)-1
    if M<D:
        M+=1
    else:
      D+=1
    if M>D:
        print("Masha")
    elif M==D:
        print("Equal")
    else:
       print("Dasha")    
       
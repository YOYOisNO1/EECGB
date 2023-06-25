    
def gcd(a,b):
        if(a%b==0):
            return b;
        return gcd(b,a%b);
    
    import math
    l,r,x,y=[int(e) for e in input().split()]
    count=0
    
    if y%x==0:
        for i in range(1,int(math.sqrt(y/x))+1):
            if (y//x)%i==0:
                if (l/x<=i<=r/x) and (l/x<=(y/x)/i<=r/x) :
    
                    if gcd(i,(y//x)/i)==1:
                        if i==(y//x)/i:
                            count+=1
                        else:
                            count+=2
        print(count);
    else:
        print("0");
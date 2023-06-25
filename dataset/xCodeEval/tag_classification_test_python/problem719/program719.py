def program719():
    from sys import stdin,stdout
    
    if __name__=="__main__":
    
        n,l,r=[int(x) for x in stdin.readline().split()]
    
        mn=0
        mx=0
    
        mn=(n-l+1)*1
    
        p=1
        for i in range(n-l+2,n+1):
            mn+=2**p
            p+=1
    
        mx=1
        if(r>1): l=2
        else: l=1
        for i in range(1,r):
            mx+=2**i
            l=2**i
        for i in range(r+1,n+1):
            mx+=l
    
        print(f"{mn} {mx}")
        
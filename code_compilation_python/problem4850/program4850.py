def lucky(x):
        s=str(x)
        return s.count('4')+s.count('7')==len(s)
    
def Gen_lucky(n):
        s=str(n)
        if(len(s)==1):
            if(s[0]=='4' or s[0]=='7'):
                return 1
            return 0
        x=0
        for i in range(1,len(s)):
            x+=2**i
        if(s[0]<'4'):
            return x
        if(s[0]>'7'):
            return x+2**len(s)
        if(s[0]=='5' or s[0]=='6'):
            return x+(2**(len(s)-1))
        if(s[0]=='7'):
            x+=2**(len(s)-1)
        x+=Getlucky(s[1:])
        return x
            
    
def Form(X,k):
        if(k==0):
            return X
        for i in range(len(X)):
            if(k>=F[len(X)-i-1]):
                h=k//F[len(X)-i-1]
                r=k%F[len(X)-i-1]
                G=list(X[i+1:])
                G.remove(X[i+h])
                G=[X[i]]+G
                return Form(X[:i]+[X[i+h]]+G,r)
    
    p=1
    
    F=[1]
    i=1
    while(p<=10**10):
        p*=i
        F.append(p)
        i+=1
    
    n,k=map(int,input().split())
    
    
        
    if(n<=15):
        L=Form(list(range(1,n+1)),k-1)
        x=0
        for i in range(n):
            if(lucky(i+1) and lucky(L[i])):
                x+=1
        print(x)
    else:
        L=Form(list(range(n-13,n+1)),k-1)
        x=Gen_lucky(n-14)
        for i in range(n-13,n+1):
            if(lucky(L[i-n+13]) and lucky(i)):
                x+=1
        print(x)
           
def program4353():
    s=input()
    a=len(s)
    b=""
    c=""
    d=""
    if a%2==0:
        a=a//2 - 1
    else:
        a=a//2
        
    i=0
    j=a+2
    
    if len(s)==1:
        print(s)
    else:
        while i<a:
            b+=s[i]
            i+=1
        while j <len(s):
            d+=s[j]
            j+=1
        while i==a or i==a+1:
            c+=s[i]
            i+=1
        print(c,end="")
        count=0
        k=0
        l=0
        e=b[::-1]
        while count<len(s)-2:
            if count%2==0:
                print(e[k],end="")
                k=k+1
            else:
                print(d[l],end="")
                l=l+1    
            
            count+=1
def program145():
    s1=(input("")).split(" ")
    n=int(s1[0])
    s=int(s1[1])
    l=[]
    sum=s
    if sum<=0 or sum>(9*n):
        if n==1 and sum==0:
            print("0 0")
        else:
            print("-1 -1")
        
    elif sum<=9*n:
        for i in range(n):
            if sum>=9:
                l.append("9")
                sum=sum-9
            elif sum<9 and sum>0:
                l.append(str(sum))
                sum=0
            elif sum==0:
                l.append("0")
        t=""
        t="".join(l)
    
        maxi=t
        j=1
        flag=1
        if t[n-1]=='0':
            j=0
    
            while t[n-1-j]=='0':
                flag=0
                j+=1
        mini=""
        if j==(n-1) and flag==0:
            for i in range(n):
                if i==0:
                    mini=mini+str((s-1))
                elif i==n-1:
                    mini=mini+"1"
                else:
                    mini=mini+"0"
            q=''.join(reversed(mini))
            
    
            print(q,maxi)
        
        elif flag==0:
            k=""
            for i in range(n):
                if i!=n-1-j and i!=n-1:
                    k=k+t[i]
                elif i==n-1-j:
                    k=k+"0"
                else:
                    k=k+t[n-1-j]
            q=''.join(reversed(k))
            f=0
            if q[0]!="1":
                f=int(q[0])-1
            h=""
            for i in range(n):
                if i==0:
                    h=h+"1"
                elif i==j:
                    h=h+str(f)
                else:
                    h=h+q[i]
            print(h) ,maxi
    
       
    
            
        else:
            for i in range(n):
                mini=mini+t[n-1-i]
            print(mini) ,maxi
    
        
    
         
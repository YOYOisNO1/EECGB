def program3328():
    ab=input().split()
    a=int(ab[0])
    b=int(ab[1])
     
    A=str(a)
    B=str(b)
      
    l='0123456789'
    l=list(l)
     
    n=0
    n1=0
    n2=0
    i=0
     
    if(len(B)==len(A)):
        while(i<len(A)):
            for k in l:
                if(n+int(k)*pow(10,len(A)-i)>=n1+int(A[i])*pow(10,len(A)-i)):
                    n+=int(k)*pow(10,len(A)-i-1)
                    n1+=int(A[i])*pow(10,len(A)-i-1)
                    l.remove(k)
                    break
            i=i+1
     
    else:
        while(i<len(A)):
            for k in l:
                if(n+int(k)*pow(10,len(A)-i)>=n1+int(A[i])*pow(10,len(A)-i)):
                    n+=int(k)*pow(10,len(A)-i-1)
                    n1+=int(A[i])*pow(10,len(A)-i-1)
                    l.remove(k)
                    break
            i=i+1
        if(n<=a):
            n='1023456789'
            n=int(n[:len(A)+1])
            
     
    if(len(A)==1):
        print(a)
    else:
        if(n>=a and n<=b):
            print(n)
        else:
            print(-1)
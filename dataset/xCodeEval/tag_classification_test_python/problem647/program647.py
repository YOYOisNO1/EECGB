def program647():
    import math
    import copy
    n=list(map(int,input()))
    
    n.reverse()
    Min=2**10
    A=copy.copy(n)
    B=copy.copy(n)
    C=copy.copy(n)
    D=copy.copy(n)
    
    if n[0]==0 and n[1]==0:
        print("0")
        exit()
    
    if n.count(0)>1:
        num=A.index(0)
        A.pop(num);A.insert(0,1)
        num+=A.index(0)-1
        A.pop(A.index(0));A.insert(1,0)
        if A[len(n)-1]==0:
            x=len(n)-1
            while A[x]==0:
                num+=1
                x-=1
        Min=min(Min,num)
        #print(num)
    
    if (0 in n) and (5 in n):
        num=B.index(0)
        B.pop(num);B.insert(0,0)
        num+=B.index(5)-1
        B.pop(B.index(5));B.insert(1,5)
        if B[len(n)-1]==0:
            x=len(n)-1
            while B[x]==0:
                num+=1
                x-=1
        Min=min(Min,num)
        #print(num)
    
    if (2 in n) and (5 in n):
        num=C.index(5)
        C.pop(num);C.insert(0,5)
        num+=C.index(2)-1
        C.pop(C.index(2));C.insert(1,2)
        if C[len(n)-1]==0:
            x=len(n)-1
            while C[x]==0:
                num+=1
                x-=1  
        Min=min(Min,num)
        #print(num)
    
    if (7 in n) and (5 in n):
        num=D.index(5)
        D.pop(num);D.insert(0,5)
        num+=D.index(7)-1
        D.pop(D.index(7));D.insert(1,7)
        x=len(n)-1
        while D[x]==0:
            num+=1  
            x-=1  
        Min=min(Min,num)
        #print(num)
    
    if Min==2**10:
        print("-1");exit()
    else:
        print(Min)
        
    
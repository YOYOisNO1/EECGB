def program180():
    #Codeforces Pages
    
    n = int(input())
    p = int(input())
    k = int(input())
    
    b = 1 if p-k<1 else p-k
    e = n if p+k>n else p+k
    
    if b !=1:
        print("<<",end=" ")
        
    for i in range(b,e+1):
        if i==p:
            print("("+str(i)+")",end=" ")
        else:
            print(i,end=" ")
    if e !=n:
        print(">>",end="")
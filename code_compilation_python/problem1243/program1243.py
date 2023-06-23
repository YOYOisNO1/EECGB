def program1243():
    input1=(list(map(int,input().split()))) 
    K=(list(map(int,input().split()))) 
    S=(list(map(int,input().split()))) 
    n=input1[0] 
    l=input1[1] 
    Klist=[] 
    for i in range(1,len(K)): 
    Klist.append(K[i]-K[i-1]) 
    max=0 
    for i in range(0,len(Klist)): 
    max+=Klist[i] 
    Klist.append(l-max) 
    Slist=[] 
    for i in range(1,len(S)): 
    Slist.append(S[i]-S[i-1]) 
    max=0 
    for i in range(0,len(Slist)): 
    max+=Slist[i] 
    Slist.append(l-max) 
    count=0 
    T=False 
    var=0 
    while count<len(Klist)+1: 
    if Slist==Klist: 
    T=True 
    break 
    else: 
    count+=1 
    var=Klist[0] 
    del Klist[0] 
    Klist.append(var) 
    if T: 
    print('YES') 
    else: 
    print('NO')
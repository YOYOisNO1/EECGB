def program4608():
    n,k=map(int,input().split())
    s=input().strip()
    markings=[]
    for i in range(n):
        markings.append(0)
    characters=set()
    for i in range(n-1,-1,-1):
        if s[i] not in characters:
            characters.add(s[i])
            markings[i]=1 
    gates=0
    characters=set()
    flag=0
    
    for i in range(n):
        if s[i] not in characters:
            characters.add(s[i])
            gates+=1 
        if gates>k:
            flag=1
            break
        if markings[i]==1:
            gates-=1 
    if gates>k:
        flag=1
    if flag==1:
        print("YES")
    else:
        print("NO")
    
            
        
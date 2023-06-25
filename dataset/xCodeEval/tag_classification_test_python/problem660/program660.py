def program660():
    inp=input()
    lst=[0]*len(inp)
    for i in range(len(inp)):
        if inp[i] in "AEIUOY":
            lst[i]=i+1
         
    jumps=[]
    last=0
         
    for i in range(len(lst)):
        if lst[i]!=0:
            jump=lst[i]-last
            jumps.append(jump)
            last=lst[i]
    
    jumps.append(len(inp)-last+1)
    if jumps == []:
        print(len(inp)+1)
    else:
        print(max(jumps))
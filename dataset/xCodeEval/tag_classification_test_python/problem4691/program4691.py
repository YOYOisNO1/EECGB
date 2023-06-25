def program4691():
    n,k=map(int,str(input()).split())
    s=str(input())
    d={}
    for i in range(65,91):
        d[chr(i)]=[0,0]
    for i in range(n):
        if d[s[i]][0]==0:
            d[s[i]][0]=i+1
        else:
            d[s[i]][1]=i+1
    for i in d:
        if d[i][0]!=0 and d[i][1]==0:
            d[i][1]=d[i][0]
    open=0
    flag=1
    for i in range(n):
        if d[s[i]][0]==i+1:
            open+=1
        if open>k:
            flag=0
        if d[s[i]][1]==i+1:
            open-=1
        if open>k:
            flag=0
        #print(d[s[i]][1],i+1)
        #print(open)
        
    if flag:
        print("NO")
    else:
        print("YES")
         
    #print(d)
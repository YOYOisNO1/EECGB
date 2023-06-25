def program3184():
    ]n,k=map(int,input().split())
    st=input()
    ans=True
    count=0
    stat={}
    last={}
    
    for i in range(n):
        last[st[i]]=i
        stat[st[i]]=False
    for i in st:
        if(stat[i]==False):
            stat[i]=True
            count+=1
        if(count>k):
            ans=False
            break
        if(last[i]==i):
            count-=1
        
        
        
        
        
    if(ans==True):
        print("NO")
    else:
        print("YES")
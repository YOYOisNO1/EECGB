def program4585():
    n,k=map(int,input().split())
    list1=input()
    s=set([])
    f=0
    for i in range(n):
        ff=0
        if(list1[i] in s):
            if(list1.find(list1[i],i+1)==-1):
                s.remove(list1[i])
        else:
            ff=1
            s.add(list1[i])
    
        if(len(s)>k):
            f=1
            break
        if(ff==1):
            if(list1.find(list1[i],i+1)==-1):
                s.remove(list1[i])
    if(f==1):
        print("YES")
    else:
        print("NO")
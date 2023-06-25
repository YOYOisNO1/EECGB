def program731():
    n=list(map(int,input().split()))
    n1=list(map(int,input().split()))
    lst=[]
    s=0
    for i in n1:
        lst.append(i)
    n1.reverse()
    for i in range(len(n1)):
        if(lst[i]!=n1[i] and lst[i]!=2 and n1[i]!=2):
            s=-1
            break
        elif(lst[i]==2 and n1[i]==0):
            lst.insert(i,0)
            lst.remove(lst[i+1])
            s=s+n[1]
        elif(lst[i]==2 and n1[i]==1):
            lst.insert(i,1)
            lst.remove(lst[i+1])
            s=s+n[2]
        else:
            if(n1[i]==2 and lst[i]==2):
                if(n[1]<n[2]):
                    lst.insert(i,0)
                    lst.remove(lst[i+1])
                    s=s+n[1]
                else:
                    lst.insert(i,1)
                    lst.remove(lst[i+1])
                    s=s+n[2]
    print(s)
        
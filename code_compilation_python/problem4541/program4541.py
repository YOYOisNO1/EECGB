def program4541():
    n,k=map(int,input().split())
    s=input()
    flag=1
    if len(s)==1:
        print(0)
    else:
        l=list(s)
        if s[0]!=1:
            l[0]=1
            k-=1
            flag=0
        #print(l)
        c=0
        if flag:
            i=0
        else:
            i=1
        #print("I",i)
        while c<k:
            if l[i]!=str(0):
                l[i]=0
                c+=1
            #print(c,k)
            i+=1
        print(''.join(str(i) for i in l))
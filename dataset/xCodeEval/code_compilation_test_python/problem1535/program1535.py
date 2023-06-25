def program1535():
    s1=input()
    w1=s1.split()
    s2=input()
    w2=s2.split()
    s3=input()
    w3=s3.split()
    n=int(w1[0])
    k=int(w1[1])
    l2=[]
    t=0
    while t<n :
        l2.append(int(w2[t])
        t+=1
    t=0
    l3=[]
    while t<k :
        l3.append(int(w3[t])
        t+=1
    i=0
    x=l2.count(0)
    while x!=0 :
        y=l2.index(0)
        l2.pop(y)
        l2.insert(y,l3[i])
        i+=1
    j=0
    while j<n-1 :
        if l2[j]>l2[j+1] :
            print("Yes")
            break
        else :
            j+=1
        if j==n-1 :
            print("No")
            break
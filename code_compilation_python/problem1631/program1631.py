def program1631():
    x=int(input())
    y=input()
    a=[]
    d1=0
    d2=[]
    m=0
    for c in x:
        x1=0
        x2=0
        s=c=="_" or c==")" or c=="("
        if s and isalpha(x[x.index(c)+1]):
            a.append(x.index(c))
            
        if c==")" and x[a[len(a)-1]]=="(":
            x1=a.[len(a)-1]+1
            x2=index(c)
            b=[]
            for i in x[x1:x2]:
                if i=="_"  and isalpha(x[x.index(i)+1]):
                   d1+=1
            for i in range((len(a)-1)):
                y1=a[i+1]-a[i]-1
                d2.append(y1)
            a=[]
    print(max(d2),d1)